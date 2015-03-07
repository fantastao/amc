function drawPie(pie){
    var myChart = echarts.init(document.getElementById(pie));
    var title = '';
    if (pie == 'pie'){
        title = '各产品销售额占比';
    }
    else {
        title = '各产品销售量占比';
    }
    var idx = 1;
    var option = {
        title : {
            text: title,
            // subtext: '',
            x:'center',
        },
        tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        color: ['#00fa9a', '#ffd700', '#6495ed', '#ff69b4', '#7b68ee'], 
        /*
        color: ['#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
            '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
                '#1e90ff', '#ff6347', '#7b68ee', '#00fa9a', '#ffd700',
                    '#6b8e23', '#ff00ff', '#3cb371', '#b8860b', '#30e0e0'], 
        */
        legend: {
            data:['Chrome','Firefox','Safari','IE9+','IE8-'],
            y: 310,
            //textStyle:{color:'auto'},
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
        calculable:true,
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
    };
    myChart.setOption(option);
}

function drawBar(bar){
    var myChart = echarts.init(document.getElementById(bar));
    var option = {
        tooltip : {
            trigger: 'axis'
        },
        legend: {
            data:['最高','高','最低','低']
        },
        color: ['#ff7f50', '#87cefa'],
        /*
        color: ['#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
            '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
                '#1e90ff', '#ff6347', '#7b68ee', '#00fa9a', '#ffd700',
                    '#6b8e23', '#ff00ff', '#3cb371', '#b8860b', '#30e0e0'], 
        */
        toolbox: {
            show : false,
            feature : {
                mark : {show: true},
                dataView : {readOnly:false},
                magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        calculable : true,
        dataZoom : {
            show : true,
            realtime : true,
            start : 40,
            end : 60
        },
        xAxis : [
            {
                type : 'category',
                boundaryGap : true,
                data : function (){
                    var list = [];
                    for (var i = 1; i <= 30; i++) {
                        list.push('2013-03-' + i);
                    }
                    return list;
                }()
            }
        ],
        yAxis : [
            {
                type : 'value',
                name : '销售额',
                axisLabel :{
                    formatter : '{value} 元'
                }
            },
            {
                type : 'value',
                name : '订单量',
                axisLabel :{
                    formatter : '{value} 件'
                }
            },
        ],
        series : [
            {
                name:'最高',
                type:'line',
                yAxisIndex: 1,
                data:function (){
                    var list = [];
                    for (var i = 1; i <= 30; i++) {
                        list.push(Math.round(Math.random()* 30) + 30);
                    }
                    return list;
                }()
            },
            {
                name:'高',
                type:'line',
                data:function (){
                    var list = [];
                    for (var i = 1; i <= 30; i++) {
                        list.push(Math.round(Math.random()* 30) + 30);
                    }
                    return list;
                }()
            },
            {
                name:'最低',
                type:'bar',
                yAxisIndex: 1,
                data:function (){
                    var list = [];
                    for (var i = 1; i <= 30; i++) {
                        list.push(Math.round(Math.random()* 10));
                    }
                    return list;
                }()
            },
            {
                name:'低',
                type:'bar',
                data:function (){
                    var list = [];
                    for (var i = 1; i <= 30; i++) {
                        list.push(Math.round(Math.random()* 10));
                    }
                    return list;
                }()
            }
        ]
    };
    /*
    var ecConfig = echarts.config;
    function eConsole(param) {
        console.log(param);
    }
    */
    /*
    myChart.on(ecConfig.EVENT.CLICK, eConsole);
    myChart.on(ecConfig.EVENT.DBLCLICK, eConsole);
    myChart.on(ecConfig.EVENT.HOVER, eConsole);
    myChart.on(ecConfig.EVENT.DATA_ZOOM, eConsole);
    myChart.on(ecConfig.EVENT.LEGEND_SELECTED, eConsole);
    myChart.on(ecConfig.EVENT.MAGIC_TYPE_CHANGED, eConsole);
    myChart.on(ecConfig.EVENT.DATA_VIEW_CHANGED, eConsole);
    */
    myChart.setOption(option);
}

drawBar('bar');
drawPie('pie');
drawPie('piepie');
