var _$ = {AJAX: function (urlparm, d, beforecall, successcall) 
    {$.ajax({ 
        url: "ashx/ajax_shoppingCart.ashx?" + urlparm, 
        data:d, 
        dataType:"Json", 
        type: "POST", 
        before: beforecall, 
        success:successcall 
        }); 
    } 
}; 
(function () { 
    var Jusoc = {}; 
    Jusoc = { 
        _inital: function () { window.Jusoc = Jusoc; }, 
        Base: {}, 
        DAO: {}, 
        BLL: {}, 
        UI: {} 
    }; 
    Jusoc.Base = { 
        Validate: { 
        } 
    }; 
    //AJAX() 
    Jusoc.DAO = { 
        Shopping: { 
            Get: function (beforecall, successcall) { 
                _$.AJAX("action=get", null, beforecall, successcall); 
            }, 
            Remove: function (pid, beforecall, successcall) { 
                _$.AJAX("action=remove", { "pid": pid }, beforecall, successcall); 
            }, 
            Add: function (pid, pcount, beforecall, successcall) { 
                _$.AJAX("action=add", { "pid": pid, "pcount": pcount }, beforecall, successcall); 
            }, 
            Set: function (pid, pcount, beforecall, successcall) { 
                _$.AJAX("action=set", { "pid": pid, "pcount": pcount }, beforecall, successcall); 
            } 
        } 
    }; 
    Jusoc.BLL = { 
        Shopping: (function () { 
            var Data = null; 
            var isLock = false; 
            var _successcall = null; 
            var _beforecall = null; 
            function Unlock() { 
                isLock = false; 
            } 
            function Lock() { 
                isLock = true; 
                if(Data&&Data !=null){ 
                    Data = null; 
                } 
            } 
            function CallBackFunction(xhr) { 
                Unlock(); 
                // if (xhr[0] == "ERROR") { 
                    // alert(xhr[1]); 
                    // return; 
                // } 
                // else if (xhr[0] == "SUCCESS") { 
                    // Jusoc.BLL.Shopping.SetData(xhr[1]); 
                // } 
                Jusoc.BLL.Shopping.SetData(xhr); 
                if (_successcall != null && _successcall) { 
                    _successcall.call(window, xhr); 
                } 
                _successcall = null; 
            } 
            function PrepareRequst(beforecall, successcall) { 
                if (isLock) { 
                    return false; 
                } 
                Lock(); 
                if (beforecall != null && beforecall) { 
                    _beforecall = beforecall; 
                } 
                if (successcall != null && successcall) { 
                    _successcall = successcall; 
                } 
            } 
            return { 
                Get: function (beforecall, successcall) { 
                    if(PrepareRequst(beforecall, successcall)==false)return false; 
                    Jusoc.DAO.Shopping.Get(_beforecall, CallBackFunction); 
                }, 
                Remove: function (pid, beforecall, successcall) { 
                    if(PrepareRequst(beforecall, successcall)==false)return false; 
                    Jusoc.DAO.Shopping.Remove(pid, _beforecall, CallBackFunction); 
                }, 
                Set: function (pid, pcount, beforecall, successcall) { 
                    if(PrepareRequst(beforecall, successcall)==false)return false; 
                    Jusoc.DAO.Shopping.Set(pid, pcount, beforecall, CallBackFunction); 
                }, 
                Add: function (pid, pcount, beforecall, successcall) { 
                    if(PrepareRequst(beforecall, successcall)==false)return false; 
                    Jusoc.DAO.Shopping.Add(pid, pcount, _beforecall, CallBackFunction); 
                }, 
                GetData: function () { 
                    //alert(Data); 
                    return Data; 
                }, 
                SetData: function (data) { Data = data; }, 
                RemoveData: function () { 
                    if (Data != null && Data) 
                        Data= null; 
                } 
            } 
        })(), 
        XHR: { 
        } 
    } 
    Jusoc.UI = { 
        ShoppingCart: (function () { 
            function Constract() { 
                Jusoc.BLL.Shopping.Get(null,SetShoppingCart); 
            } 
            function SetShoppingCart(data) { 
                //这里来填充购物车中的数据 
                var data = Jusoc.BLL.Shopping.GetData(); 
                //这里 先构建 整个的购物车 
                var html = "<table class=\"shoppingcart-list\" id=\"sm\">"+ 
                "<tr>"+ 
                "<th>"+ 
                "书啊"+ 
                "</th>"+ 
                "<th>"+ 
                "书名"+ 
                "</th>"+ 
                "<th>"+ 
                " 单价"+ 
                "</th>"+ 
                "<th>"+ 
                " 数量"+ 
                "</th>"+ 
                "<th>"+ 
                " 操作"+ 
                "</th>"+ 
                "</tr>"; 
                for(var i =0;i<data.length;i++) 
                    { 
                        html += "<tr>"+ 
                        "<td>"+ 
                        "<img src=\"ss\" height=\"36px\" width=\"28px\"/>"+ 
                        "</td>"+ 
                        "<td>"+ 
                        data[i].Name+ 
                        "</td>"+ 
                        "<td>"+ 
                        "￥"+data[i].Money+ 
                        "</td>"+ 
                        "<td>"+ 
                        "<div class=\"item-change\">"+ 
                        "<input type=\"text\" value='"+data[i].Count+"' />"+ 
                        "<span title=\"数量加一\" class=\"add\" onclick=\"Jusoc.UI.ShoppingCart.Plus(1,this.parentNode.childNodes[0].value,this.parentNode.childNodes[0])\"></span> <span "+ 
                        "title=\"数量减一\" class=\"cut\" onclick=\"Jusoc.UI.ShoppingCart.Minus(1,this.parentNode.childNodes[0].value,this.parentNode.childNodes[0])\"></span>"+ 
                        "</div>"+ 
                        "</td>"+ 
                        "<td>"+ 
                        "<span class=\"RemoveLink\" onclick=\"Jusoc.UI.ShoppingCart.Remove(1,this.parentNode.parentNode)\">Remove From Cark</span>"+ 
                        "</td>"+ 
                        "</tr>"; 
                    } 
                    html+="</table>"; 
                    document.body.innerHTML+=html; 
            } 
            function AddToPanel(data) { 
                //这里是对 添加一个商品到购物车 来修改前台样式 
                var obj = document.getElementById("sm"); 
                var html = "<td>"+ 
                "<img src=\"soo\" height=\"36px\" width=\"28px\"/>"+ 
                "</td>"+ 
                "<td>"+ 
                data.Name+ 
                "</td>"+ 
                "<td>"+ 
                "￥"+data.Money+ 
                "</td>"+ 
                "<td >"+ 
                "<div class=\"item-change\">"+ 
                "<input type=\"text\" value='"+data.Count+"' />"+ 
                "<span title=\"数量加一\" class=\"add\" onclick=\"Jusoc.UI.ShoppingCart.Plus(1,this.parentNode.childNodes[0].value,this.parentNode.childNodes[0])\"></span> <span "+ 
                "title=\"数量减一\" class=\"cut\" onclick=\"Jusoc.UI.ShoppingCart.Minus(1,this.parentNode.childNodes[0].value,this.parentNode.childNodes[0])\"></span>"+ 
                "</div>"+ 
                "</td>"+ 
                "<td>"+ 
                "<span class=\"RemoveLink\" onclick=\"Jusoc.UI.ShoppingCart.Remove(1,this.parentNode.parentNode)\">Remove From Cark</span>"+ 
                "</td>"; 
                var row = obj.insertRow(1); 
                row.innerHTML = html; 
                return; 
                obj.childNodes[0].innerHTML += html; 
            } 
            function UpdatePanel(obj, count) { 
                //这里是从购物车中 增加 或者 减少 修改操作 
                obj.value = count; 
            } 
            function RemoveFromPanel(child) 
            { 
                var obj = document.getElementById("sm"); 
                obj.childNodes[0].removeChild(child); 
            } 
            return { 
                PageLoad: function () { 
                    Constract(); 
                }, 
                Add: function (pid, pcount) { 
                    Jusoc.BLL.Shopping.Add(pid,pcount, null, AddToPanel); 
                }, 
                Plus: function (pid, pcount, obj) { 
                    pcount = parseInt(pcount) + 1; 
                    Jusoc.BLL.Shopping.Set(pid, pcount, function () { alert("before") }, function (data) { UpdatePanel(obj, pcount) }); 
                }, 
                Minus:function(pid,pcount,obj){ 
                    pcount = parseInt(pcount) - 1; 
                    Jusoc.BLL.Shopping.Set(pid,pcount,null,function(data){ UpdatePanel(obj,pcount)}); 
                }, 
                Remove:function(pid,obj){ 
                    Jusoc.BLL.Shopping.Remove(pid,null,function(data){ RemoveFromPanel(obj);}); 
                } 
            } 
        })() 
    } 
    Jusoc._inital(); 
})() 


