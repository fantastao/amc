function drawBar(){
    var myChart = echarts.init(document.getElementById('bar'));
    var option = {
        tooltip : {
            trigger: 'axis'
        },
        toolbox: {
            show : false,
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        calculable : true,
        legend: {
            data:['蒸发量','降水量','平均温度']
        },
        xAxis : [
            {
                type : 'category',
                data : ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
            }
        ],
        yAxis : [
            {
                type : 'value',
                name : '水量',
                axisLabel : {
                    formatter: '{value} ml'
                }
            },
            {
                type : 'value',
                name : '温度',
                axisLabel : {
                    formatter: '{value} °C'
                }
            }
        ],
        series : [
            {
                name:'蒸发量',
                type:'bar',
                data:[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
            },
            {
                name:'降水量',
                type:'bar',
                data:[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
            },
            {
                name:'平均温度',
                type:'line',
                yAxisIndex: 1,
                data:[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
            }
        ]
    };
    myChart.setOption(option);
}
function drawPie(){
    var myChart = echarts.init(document.getElementById('pie'));
    var idx = 1;
    var option = {
        timeline : {
            data : [
                '2013-01-01', '2013-02-01', '2013-03-01', '2013-04-01', '2013-05-01',
                { name:'2013-06-01', symbol:'emptyStar6', symbolSize:8 },
                '2013-07-01', '2013-08-01', '2013-09-01', '2013-10-01', '2013-11-01',
                { name:'2013-12-01', symbol:'star6', symbolSize:8 }
            ],
            label : {
                formatter : function(s) {
                    return s.slice(0, 7);
                }
            }
        },
        options : [
            {
                title : {
                    text: '',
                    subtext: ''
                },
                tooltip : {
                    trigger: 'item',
                    formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                    data:['Chrome','Firefox','Safari','IE9+','IE8-']
                },
                toolbox: {
                    show : false,
                    feature : {
                        mark : {show: true},
                        dataView : {show: true, readOnly: false},
                        magicType : {
                            show: true, 
                            type: ['pie', 'funnel'],
                            option: {
                                funnel: {
                                    x: '25%',
                                    width: '50%',
                                    funnelAlign: 'left',
                                    max: 1700
                                }
                            }
                        },
                        restore : {show: true},
                        saveAsImage : {show: true}
                    }
                },
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        center: ['50%', '45%'],
                        radius: '50%',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            },
            {
                series : [
                    {
                        name:'浏览器（数据纯属虚构）',
                        type:'pie',
                        data:[
                            {value: idx * 128 + 80,  name:'Chrome'},
                            {value: idx * 64  + 160,  name:'Firefox'},
                            {value: idx * 32  + 320,  name:'Safari'},
                            {value: idx * 16  + 640,  name:'IE9+'},
                            {value: idx++ * 8  + 1280, name:'IE8-'}
                        ]
                    }
                ]
            }
        ]
    };
    myChart.setOption(option);
}
function drawNetwork(){
    var myChart = echarts.init(document.getElementById('network'));
    var option = {
        title : {
            text: '人物关系：乔布斯',
            subtext: '数据来自人立方',
            x:'right',
            y:'bottom'
        },
        tooltip : {
            trigger: 'item',
            formatter: '{a} : {b}'
        },
        toolbox: {
            show : true,
            feature : {
                restore : {show: true},
                magicType: {show: true, type: ['force', 'chord']},
                saveAsImage : {show: true}
            }
        },
        legend: {
            x: 'left',
            data:['家人','朋友']
        },
        series : [
            {
                type:'force',
                name : "人物关系",
                ribbonType: false,
                categories : [
                    {
                        name: '人物'
                    },
                    {
                        name: '家人'
                    },
                    {
                        name:'朋友'
                    }
                ],
                itemStyle: {
                    normal: {
                        label: {
                            show: true,
                            textStyle: {
                                color: '#333'
                            }
                        },
                        nodeStyle : {
                            brushType : 'both',
                            borderColor : 'rgba(255,215,0,0.4)',
                            borderWidth : 1
                        },
                        linkStyle: {
                            type: 'curve'
                        }
                    },
                    emphasis: {
                        label: {
                            show: false
                            // textStyle: null      // 默认使用全局文本样式，详见TEXTSTYLE
                        },
                        nodeStyle : {
                            //r: 30
                        },
                        linkStyle : {}
                    }
                },
                useWorker: false,
                minRadius : 15,
                maxRadius : 25,
                gravity: 1.1,
                scaling: 1.1,
                roam: 'move',
                nodes:[
                    {category:0, name: '乔布斯', value : 10, label: '乔布斯\n（主要）'},
                    {category:1, name: '丽萨-乔布斯',value : 2},
                    {category:1, name: '保罗-乔布斯',value : 3},
                    {category:1, name: '克拉拉-乔布斯',value : 3},
                    {category:1, name: '劳伦-鲍威尔',value : 7},
                    {category:2, name: '史蒂夫-沃兹尼艾克',value : 5},
                    {category:2, name: '奥巴马',value : 8},
                    {category:2, name: '比尔-盖茨',value : 9},
                    {category:2, name: '乔纳森-艾夫',value : 4},
                    {category:2, name: '蒂姆-库克',value : 4},
                    {category:2, name: '龙-韦恩',value : 1},
                ],
                links : [
                    {source : '丽萨-乔布斯', target : '乔布斯', weight : 1, name: '女儿'},
                    {source : '保罗-乔布斯', target : '乔布斯', weight : 2, name: '父亲'},
                    {source : '克拉拉-乔布斯', target : '乔布斯', weight : 1, name: '母亲'},
                    {source : '劳伦-鲍威尔', target : '乔布斯', weight : 2},
                    {source : '史蒂夫-沃兹尼艾克', target : '乔布斯', weight : 3, name: '合伙人'},
                    {source : '奥巴马', target : '乔布斯', weight : 1},
                    {source : '比尔-盖茨', target : '乔布斯', weight : 6, name: '竞争对手'},
                    {source : '乔纳森-艾夫', target : '乔布斯', weight : 1, name: '爱将'},
                    {source : '蒂姆-库克', target : '乔布斯', weight : 1},
                    {source : '龙-韦恩', target : '乔布斯', weight : 1},
                    {source : '克拉拉-乔布斯', target : '保罗-乔布斯', weight : 1},
                    {source : '奥巴马', target : '保罗-乔布斯', weight : 1},
                    {source : '奥巴马', target : '克拉拉-乔布斯', weight : 1},
                    {source : '奥巴马', target : '劳伦-鲍威尔', weight : 1},
                    {source : '奥巴马', target : '史蒂夫-沃兹尼艾克', weight : 1},
                    {source : '比尔-盖茨', target : '奥巴马', weight : 6},
                    {source : '比尔-盖茨', target : '克拉拉-乔布斯', weight : 1},
                    {source : '蒂姆-库克', target : '奥巴马', weight : 1}
                ]
            }
        ]
    };
    myChart.setOption(option);
    /*
    var ecConfig = echarts.config;
    function focus(param) {
        var data = param.data;
        var links = option.series[0].links;
        var nodes = option.series[0].nodes;
        if (data.source !== undefined && data.target !== undefined)
        { //点击的是边
            var sourceNode = nodes.filter(function (n) {return n.name == data.source})[0];
            var targetNode = nodes.filter(function (n) {return n.name == data.target})[0];
            console.log("选中了边 " + sourceNode.name + ' -> ' + targetNode.name + ' (' + data.weight + ')');
        } else { // 点击的是点
            console.log("选中了" + data.name + '(' + data.value + ')');
        }
    }
    myChart.on(ecConfig.EVENT.CLICK, focus)

    myChart.on(ecConfig.EVENT.FORCE_LAYOUT_END, function () {
        console.log(myChart.chart.force.getPosition());
    });
    */
}
function drawDynamicBar(){
    var myChart = echarts.init(document.getElementById('dynamic_bar'));
    var option = {
        title : {
            text: '',
            subtext: ''
        },
        tooltip : {
            trigger: 'axis'
        },
        legend: {
            data:['最新成交价', '预购队列']
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                magicType : {show: true, type: ['line', 'bar']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        dataZoom : {
            show : false,
            start : 0,
            end : 100
        },
        xAxis : [
            {
                type : 'category',
                boundaryGap : true,
                data : (function (){
                    var now = new Date();
                    var res = [];
                    var len = 10;
                    while (len--) {
                        res.unshift(now.toLocaleTimeString().replace(/^\D*/,''));
                        now = new Date(now - 2000);
                    }
                    return res;
                })()
            },
            {
                type : 'category',
                boundaryGap : true,
                data : (function (){
                    var res = [];
                    var len = 10;
                    while (len--) {
                        res.push(len + 1);
                    }
                    return res;
                })()
            }
        ],
        yAxis : [
            {
                type : 'value',
                scale: true,
                name : '价格',
                boundaryGap: [0.2, 0.2]
            },
            {
                type : 'value',
                scale: true,
                name : '预购量',
                boundaryGap: [0.2, 0.2]
            }
        ],
        series : [
            {
                name:'预购队列',
                type:'bar',
                xAxisIndex: 1,
                yAxisIndex: 1,
                data:(function (){
                    var res = [];
                    var len = 10;
                    while (len--) {
                        res.push(Math.round(Math.random() * 1000));
                    }
                    return res;
                })()
            },
            {
                name:'最新成交价',
                type:'line',
                data:(function (){
                    var res = [];
                    var len = 10;
                    while (len--) {
                        res.push((Math.random()*10 + 5).toFixed(1) - 0);
                    }
                    return res;
                })()
            }
        ]
    };
    myChart.setOption(option);
    var lastData = 11;
    var axisData;
    timeTicket = setInterval(function (){
        lastData += Math.random() * ((Math.round(Math.random() * 10) % 2) == 0 ? 1 : -1);
        lastData = lastData.toFixed(1) - 0;
        axisData = (new Date()).toLocaleTimeString().replace(/^\D*/,'');

        // 动态数据接口 addData
        myChart.addData([
            [
                0,        // 系列索引
                Math.round(Math.random() * 1000), // 新增数据
                true,     // 新增数据是否从队列头部插入
                false     // 是否增加队列长度，false则自定删除原有数据，队头插入删队尾，队尾插入删队头
            ],
            [
                1,        // 系列索引
                lastData, // 新增数据
                false,    // 新增数据是否从队列头部插入
                false,    // 是否增加队列长度，false则自定删除原有数据，队头插入删队尾，队尾插入删队头
                axisData  // 坐标轴标签
            ]
        ]);
    }, 2000);
    //clearInterval(timeTicket);
}
drawBar();
drawPie();
drawNetwork();
drawDynamicBar();
