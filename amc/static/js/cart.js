function call_ajax_request(url, callback){
    $.ajax({
        url: url,
        dataType: "json",
        method: "get",
        success: callback
    });
}

function drawItems(data){
    $("#items_list").empty();
    var html = '';
    if (data.length == 0){
        //html += '<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>';
        html += '您还没有添加产品到购物车!';
        $("#message").prepend(html);
    }
    else{
        for (var i=0;i<data.length;i++){
            var product = data[i];
            html += '<tr>'
            html += '<td><a href="/product/' + product["product_id"] +'">' + product["product_id"] + '</a></td>';
            html += '<td><a href="/product/' + product["product_id"] +'">' + product["name"] + '</a></td>';
            html += '<td>' + product["price"] + '</td>';
            html += '<td class="text-center vert-align"><input onchange="itemsUpdate(' + product["product_id"] + ',this.value);" type="number" min="1" style="width:50px;" value="' + product["quantity"] +'"></td>';
            html += '<td class="text-right vert-align">' + product["price"] * product["quantity"] + '</td>';
            html += '<td class="text-center vert-align"><a><span class="glyphicon glyphicon-remove" onclick="itemsDelete(' + product["product_id"] + ');"></span></a></td>';
            html += '</tr>';
        }
        $("#items_list").html(html);
    }
    products2total(data);
}

function products2total(data){
    var total = 0;
    if (data.length > 0){
        for (var i=0;i<data.length;i++){
            var product = data[i];
            total += product["price"] * product["quantity"];
        }
    }
    drawTotal(total);
}
function drawTotal(total){
    $("#items_total").empty();
    var transport;
    if (total == 0){
        transport = 0;
    }else{
        transport = 0;
    }
    var fax = 0;
    var cost = total + transport - fax;
    var html = '';
    html += '<tr>';
    html += '<td>商品总额：</td>';
    html += '<td></td>';
    html += '<td class="text-right"><b class="ng-binding">' + total + '</b></td>';
    html += '</tr><tr>';
    html += '<td>运费：</td>';
    html += '<td></td>';
    html += '<td class="text-right ng-binding">' + transport + '</td>';
    html += '</tr><tr>';
    html += '<td>税费：</td>';
    html += '<td></td>';
    html += '<td class="text-right ng-binding">' + fax + '</td>';
    html += '</tr><tr>';
    html += '<td>合计：</td>';
    html += '<td></td>';
    html += '<td class="text-right ng-binding">' + cost + '</td>';
    html += '</tr>';
    $("#items_total").html(html);
}
function itemsUpdate(product_id, product_quantity){
    data = {"product_quantity": parseInt(product_quantity)}
    url = "/apis/open/trolley/" + product_id + "/"
    $.ajax({
        url: url,
        type: "put",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType:"json",
        async: true,
    });
}
function itemsDelete(product_id){
    url = "/apis/open/trolley/" + product_id + "/"
    $.ajax({
        url: url,
        type: "delete",
        dataType:"json",
        async: true,
    });
}

call_ajax_request('/trolley/items/', drawItems);
