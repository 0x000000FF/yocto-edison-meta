// JavaScript source code]
var x = 0;
var y = 0;
var z = 0;
var xmax = 200;
var ymax = 180;
var zmax = 180;
var cmd_str;
function movexyz(axis, num) {
    $.get('./send/G91', function (data) {
        //alert('1\n' + data);
    });
    switch (axis) {
        case 'xh':
            x = 0;
            cmd_str = 'G28 X0';
            break;
        case 'yh':
            y = 0;
            cmd_str = 'G28 Y0';
            break;
        case 'zh':
            z = 0;
            cmd_str = 'G28 Z0';
            break;
        case 'all':
            x = 0;
            y = 0;
            z = 0;
            cmd_str = 'G28';
            break;
        case 'x':
            x = x + parseInt(num);
            if (x < 0) x = 0;
            if (x > xmax) x = xmax;
            cmd_str = "G1 F4000 X" + num;
            break;
        case 'y':
            y = y + parseInt(num);
            if (y < 0) y = 0;
            if (y > ymax) y = ymax;
            cmd_str = "G1 F4000 Y" + num;
            break;
        case 'z':
            z = z + parseInt(num);
            if (z < 0) z = 0;
            if (z > zmax) z = zmax;
            cmd_str = "G1 F4000 Z" + num;
            break;
        case 'e0':
            $.get('./get/extrudertemp', function (data) {
                if (data < 170) {
                    if (lang == 'zh') {
                        msg = '加热不足';
                    } else {
                        msg = 'Underheat';
                    }
                    $.notify({
                        message: msg,
                        status: 'warning',
                        timeout: 5000
                    });
                }
                else if (num < 0) {
                    cmd_str = "G1 F1800 E" + num;
                }
                else {
                    cmd_str = "G1 F120 E" + num;
                }
            });
            break;
        default:
            cmd_str = '';
    }
    if (cmd_str != '') {
        //alert('2\n' + cmd_str);
        $.get('./send/' + cmd_str, function (data) {
            if (lang == 'zh') {
                msg = '移动到X: ';
            } else {
                msg = 'Move to X : ';
            }
            $.notify({
                message: msg + x + ' Y:' + y + ' Z:' + z,
                status: 'info',
                timeout: 2000
            });
        });
    }
    cmd_str = '';

}
//控制面板回车执行查询
$('#input_cmd').bind('keyup', function (event) {
    if (event.keyCode == "13") {
        var key = $("#input_cmd").val();
        send(key);
    }
});

$('#Send').click(function () {
    var key = $("#input_cmd").val();
    send(key);
});
//控制面板点击进行查询
function send(cmd) {
    $.get('./send/' + cmd, function (data) {
        if (lang == 'zh') {
            msg = ' 操作成功';
        } else {
            msg = ' Send success';
        }
        $.notify({
            message: cmd + ' ' + msg,
            status: 'info',
            timeout: 2000
        });
        $('#input_cmd').val('');
    });
}