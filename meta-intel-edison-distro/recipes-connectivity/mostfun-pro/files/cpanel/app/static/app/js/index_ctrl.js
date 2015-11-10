/**
 * Created by Administrator on 2015/8/15.
 */
$("#ctl_1").click(function (e) {
    var X = ((e.pageX - $("#ctl_1").offset().left) / $("#ctl_1").width()) * 200 - 100;
    var Y = ((e.pageY - $("#ctl_1").offset().top) / $("#ctl_1").height()) * 200 - 100;
    var Y = -Y;
//圆的半径
    var R = math.sqrt(X * X + Y * Y);
    var angle = math.asin(Y / R);
//获取XY正负区域
    if (angle) {
        if ((angle <= 0.770) && (X > 0) && (angle >= -0.770) && (R < 88)) {//+X
            if (R <= 32) {
                movexyz('x', '1');
            }
            else if ((R > 32) && (R <= 70)) {
                movexyz('x', '10');
            }
            else if ((R > 70) && (R <= 88)) {
                movexyz('x', '50');
            }
        }
        else if ((angle > 0.770) && (angle <= 1.57) && (R < 88)) {//+Y
            if (R <= 32) {
                movexyz('y', '1');
            }
            else if ((R > 32) && (R <= 70)) {
                movexyz('y', '10');
            }
            else if ((R > 70) && (R <= 88)) {
                movexyz('y', '50');
            }
        }
        else if ((angle <= 0.770) && (X < 0) && (angle >= -0.770 && (R < 88))) {//-X
            if (R <= 32) {
                movexyz('x', '-1');
            }
            else if ((R > 32) && (R <= 70)) {
                movexyz('x', '-10');
            }
            else if ((R > 70) && (R <= 88)) {
                movexyz('x', '-50');
            }
        }
        else if ((angle < -0.770) && (angle >= -1.57) && (R < 88)) {//-Y
            if (R <= 32) {
                movexyz('y', '-1');
            }
            else if ((R > 32) && (R <= 70)) {
                movexyz('y', '-10');
            }
            else if ((R > 70) && (R <= 88)) {
                movexyz('y', '-50');
            }
        }
    }
//获取区域
    if (R) {
        if ((R > 88) && (X > 0) && (Y > 0)) {
            movexyz('zh', '0');
            $("#ctl_1").attr("title", "z-Home");
        }//z-Home
        if ((R > 88) && (X > 0) && (Y < 0)) {
            movexyz('xh', '0');
            $("#ctl_1").attr("title", "x-Home");
        }//x-Home
        if ((R > 88) && (X < 0) && (Y > 0)) {
            movexyz('yh', '0');
            $("#ctl_1").attr("title", "y-Home");
        }//y-Home
        if ((R > 88) && (X < 0) && (Y < 0)) {
            movexyz('all', '0');
            $("#ctl_1").attr("title", "Home");
        }//Home
    }
});
//鼠标移动到此处有文字出现
$("#ctl_1").mousemove(function (e) {
    var X = ((e.pageX - $("#ctl_1").offset().left) / $("#ctl_1").width()) * 200 - 100;
    var Y = ((e.pageY - $("#ctl_1").offset().top) / $("#ctl_1").height()) * 200 - 100;
    var Y = -Y;
    var R = math.sqrt(X * X + Y * Y);
    if ((R > 88) && (X > 0) && (Y > 0)) {
        $("#ctl_1").attr("title", "z-Home");
    }//z-Home
    if ((R > 88) && (X > 0) && (Y < 0)) {
        $("#ctl_1").attr("title", "x-Home");
    }//x-Home
    if ((R > 88) && (X < 0) && (Y > 0)) {
        $("#ctl_1").attr("title", "y-Home");
    }//y-Home
    if ((R > 88) && (X < 0) && (Y < 0)) {
        $("#ctl_1").attr("title", "Home");
    }//Home
});
//图 ctl-2
$("#ctl_2").click(function (e) {
    var Y = ((e.pageY - $("#ctl_2").offset().top) / $("#ctl_2").height()) * 160 - 80;
    var Y = -Y;
    //$("#log").text("X:" + X + ",Y:" + Y);
//获取区域
    if ((Y > 0) && (Y < 12 )) {
        movexyz('z', '1');
    }
    if ((Y > 10 ) && (Y < 33)) {
        movexyz('z', '10');
    }
    if ((Y > 33 ) && (Y < 54)) {
        movexyz('z', '50');
    }
    if ((Y < 0) && (Y > -10 )) {
        movexyz('z', '-1')
    }
    if ((Y < -10 ) && (Y > -31 )) {
        movexyz('z', '-10');
    }
    if ((Y < -31) && (Y > -53 )) {
        movexyz('z', '-50');
    }
});
//图 ctl-3
$("#ctl_3").click(function (e) {
    var Y = ((e.pageY - $("#ctl_3").offset().top) / $("#ctl_3").height()) * 160 - 80;
    var Y = -Y;
    //$("#log").text("X:" + X + ",Y:" + Y);
//获取区域
    if ((Y > 0) && (Y < 12 )) {
        movexyz('z', '1');
    }
    if ((Y > 10 ) && (Y < 33)) {
        movexyz('z', '10');
    }
    if ((Y > 33 ) && (Y < 54)) {
        movexyz('z', '50');
    }
    if ((Y < 0) && (Y > -10 )) {
        movexyz('z', '-1')
    }
    if ((Y < -10 ) && (Y > -31 )) {
        movexyz('z', '-10');
    }
    if ((Y < -31) && (Y > -53 )) {
        movexyz('z', '-50');
    }
});

$('#noz_heat_chk').change(function () {
    if ($('#noz_heat_chk').is(':checked')) {
        data = 'M104 T0 S' + $('#ctl_noz .tooltip-inner').text();
    } else {
        data = 'M104 T0 S0';
    }
    send(data);
});

$('#bed_heat_chk').change(function () {
    if ($('#bed_heat_chk').is(':checked')) {
        data = 'M190 S' + $('#ctl_bed .tooltip-inner').text();
    } else {
        data = 'M190 S0';
    }
    send(data);
});

$(document).ready(function () {
    $('div[data=roll]').click(function () {
        pid = $(this).parent().parent().attr('id');
        if (pid == 'ctl_noz') {
            if ($('#noz_heat_chk').is(':checked')) {
                cmd = 'M104 T0 S' + $('#ctl_noz .tooltip-inner').text();
            }
        }
        else if (pid == 'ctl_bed') {
            if ($('#bed_heat_chk').is(':checked')) {
                cmd = 'M190 S' + $('#ctl_bed .tooltip-inner').text();
            }
        } else {
            return;
        }
        send(cmd);
    });
});
