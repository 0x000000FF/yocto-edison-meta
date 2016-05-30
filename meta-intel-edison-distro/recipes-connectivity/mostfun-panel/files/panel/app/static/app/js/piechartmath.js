$(function(){
    //var title_index=$('#title_index');
    //var title_fielMg=$('#title_fielMg');
    //var title_getmodel=$('#title_getmodel');
    //var title_set=$('#title_set');
    //var title_guide=$('#title_guide');
    //
    //title_index.on('click',function(){
    //    $('#baseContent').attr('src','index2.html');
    //});

    $.ajax({
        type:"get",
        url:"/space-left",
        dataType:"json",
        success:function(_data){
            //Object {total: "1337936", used: "10548"}
            //定义转换进制
            var toPercent=100;
            var toShowUsage=5;
            var total=parseInt(_data['total']);
            var used=parseInt(_data['used']);
            //转换成百分比并保留两位小数
            var usage=((used/total)*toPercent).toFixed(2);
            var $filerain=$('#file-rain');

            var total2=bytesToSize(total);
            var used2=bytesToSize(used);
            var usagesEnd=Math.ceil(usage/toShowUsage);

            $filerain.attr('data-label',usage.toString()+'%');

            $('#rain-usage').html(usage.toString());
            $('#rain-used').html(used2.toString());
            $('#rain-total').html(total2.toString());
            //模板再带以五为进制显示
            if(usagesEnd*toShowUsage<=100){
                $filerain.addClass("radial-bar-"+(usagesEnd*toShowUsage).toString());
            }else{
                $filerain.addClass("radial-bar-100");
            }
        }
    });
            //进制换算方法
            function bytesToSize(bytes) {
                    if (bytes === 0) return '0 B';
                    var k = 1000, // or 1024
                    sizes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                    i = Math.floor(Math.log(bytes) / Math.log(k));
                    return (bytes / Math.pow(k, i)).toPrecision(3) + ' ' + sizes[i];
            }
});