function drawPie(pie, title, legend_name, series_data){
    var myChart = echarts.init(document.getElementById(pie));
    var idx = 1;
    var option = {
        title : {
            text: title,
            // subtext: '',
            x:'center',
        },
        tooltip : {
            trigger: 'item',
            formatter: "{b} : {c} ({d}%)"
        },
        color: ['#00fa9a', '#ffd700', '#6495ed', '#ff69b4', '#7b68ee'], 
        /*
        color: ['#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
            '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
                '#1e90ff', '#ff6347', '#7b68ee', '#00fa9a', '#ffd700',
                    '#6b8e23', '#ff00ff', '#3cb371', '#b8860b', '#30e0e0'], 
        */
        legend: {
            data: legend_name,
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
                type:'pie',
                center: ['50%', '45%'],
                radius: '50%',
                data: series_data,
            }
        ]
    };
    myChart.setOption(option);
}

function drawBar(bar, series, xAxis){
    var myChart = echarts.init(document.getElementById(bar));
    var option = {
        tooltip : {
            trigger: 'axis',
            formatter: "{b}<br/>{a0}：{c0}<br/>{a1}：{c1}",
        },
        legend: {
            data:['销售额','订单量']
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
            start : 20,
            end : 80,
        },
        xAxis : xAxis,
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
        series : series,
    };
    myChart.setOption(option);
}

function bar_callback(bar_data){
    var time_list = [];
    var order_bar_list = [];
    var order_line_list = [];
    var income_bar_list = [];
    var income_line_list = [];
    for (var date in bar_data){
        time_list.push(date);
        order_bar_list.push(bar_data[date][0])
        order_line_list.push(bar_data[date][0])
        income_bar_list.push(bar_data[date][1])
        income_line_list.push(bar_data[date][1])
    }
    var series = [
        {
            name:'销售额',
            type:'bar',
            data: income_bar_list,
        },
        {
            name:'订单量',
            type:'bar',
            yAxisIndex: 1,
            data: order_bar_list,
        },
        {
            name:'销售额',
            type:'line',
            data: income_line_list,
        },
        {
            name:'订单量',
            type:'line',
            yAxisIndex: 1,
            data: order_line_list,
        }
    ];
    var xAxis = [
        {
            type : 'category',
            boundaryGap : true,
            data: time_list,
        }
    ];
    drawBar(bar_div, series, xAxis);
}

function series_sort(a,b){
    return b['value'] - a['value'];
}

function pie_limit(series_data){
    if (series_data.length > TOP_LIMIT){
        var total = 0;
        for (var i = TOP_LIMIT;i < series_data.length;i++){
            total += series_data[i]['value'];
        }
        var last = {
            name: '其它',
            value: total
        };
        series_data[TOP_LIMIT] = last;
    }
    return series_data;
}

function pie_callback(pie_data){
    var order_title = '产品销售量占比';
    var income_title = '产品销售额占比';
    var order_legend_name = [];
    var income_legend_name = [];
    var order_series_data = [];
    var income_series_data = [];
    for (var product_id in pie_data){
        var product = pie_data[product_id];
        order_series_data.push({
            name: product[0],
            value: product[1],
        });
        income_series_data.push({
            name: product[0],
            value: product[2],
        });
    }
    var length = Math.min(TOP_LIMIT, income_series_data.length); // 最多取前五个产品
    
    if (length == 0){
        drawPie(pie_div, income_title, income_legend_name, income_series_data);
        drawPie(pie_pie_div, order_title, order_legend_name, order_series_data);
        return;
    }
    
    income_series_data.sort(series_sort);
    income_series_data = pie_limit(income_series_data);

    for (var i = 0;i < length; i++){
        income_legend_name.push(income_series_data[i]['name']);
    }
    drawPie(pie_div, income_title, income_legend_name, income_series_data);

    order_series_data.sort(series_sort);
    order_series_data = pie_limit(order_series_data);
    for (var i = 0;i < length; i++){
        order_legend_name.push(order_series_data[i]['name']);
    }
    drawPie(pie_pie_div, order_title, order_legend_name, order_series_data);
}

function call_ajax_request(url, callback){
    $.ajax({
        url: url,
        type: "get",
        dataType: "json",
        async: true,
        success: callback
    })
}

var bar_div = 'bar';
var pie_div = 'pie';
var pie_pie_div = 'piepie';
var TOP_LIMIT = 5;
var bar_url = "/apis/panel/index_bar_chart/";
var pie_url = "/apis/panel/index_pie_chart/";
call_ajax_request(bar_url, bar_callback);
call_ajax_request(pie_url, pie_callback);
