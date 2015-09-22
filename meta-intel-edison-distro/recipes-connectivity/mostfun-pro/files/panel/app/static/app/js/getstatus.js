// JavaScript source code]
var layecount = 0;
var layenum = 0;
var status = 0;

var laynow = '';
var layper = '';
var ptrnme = '';
var laycnt = '';

$(document).ready(function () {
    laynow = $("#info_layenow").text();
    layper = $("#info_layeper").text();
    ptrnme = $("#info_ptrname").text();
    laycnt = $("#info_layecount").text();
});

var msg = '';
function getlaye() {
    $.get('./get/layernum', function (data) {

        $("#info_layenow").text(laynow + "：" + data);
        par = (parseInt(data) * 100) / layecount;
        $("#info_layeper").text(layper + "：" + par.toFixed(2) + '%');
        if (parseInt(data) == (layecount - 1)) {
            $.getJSON('./get/state', function (json) {
                status = json[0];
                if (status == 'ready') {
                    if (lang == 'zh') {
                        msg = '打印完成!';
                    } else {
                        msg = 'Finish !';
                    }
                    $.notify({
                        message: msg,
                        status: 'info'
                    });
                    $("#filetable").show();
                    $("#mac_ctrl").show();
                    $("#info_status").hide();
                }
            });
        }
    });
    if (status != 'ready')
        setTimeout(getlaye, 5000);
}

function getstatus() {
    $.getJSON('./get/state', function (json) {
        status = json[0];
        if (status == 'ready') {
            $("#filetable").show();
            $("#mac_ctrl").show();
            //$("#info_status").hide();
            if (lang == 'zh') {
                msg = 'mostfun Pro 准备就绪!';
            } else {
                msg = 'mostfun Pro is ready !';
            }
            $.notify({
                message: msg,
                status: 'info'
            });
        }
        else {
            if (lang == 'zh') {
                msg = 'mostfun Pro 正在打印!';
            } else {
                msg = 'mostfun Pro is printing !';
            }
            $.notify({
                message: msg,
                status: 'info'
            });
            $("#filetable").hide();
            $("#mac_ctrl").hide();
            $("#info_status").show();
            $.get('./get/layernum', function (data) {
                if (data >= 0) data = 0;
                layenum = parseInt(data);
            });
            $("#mod_img").attr("src", './model/' + json[1].replace(".gcode", ".jpg"));
            $("#info_ptrname").text(ptrnme + "：" + json[1].replace(".gcode", ""));

            $("#info_layecount").text(laycnt + "：" + json[2]);
            layecount = parseInt(json[2]);
            $("#info_layenow").text(laynow + "：");

            $("#info_layeper").text(layper + "：");
            getlaye();
            //var timer_getlaye = setInterval(getlaye, 5000);
        }
    });
}

$('#but_prt').click(function () {//暂停/继续打印文件
    var btntext = '';
    var btnnewtext = '';
    if (lang == 'zh') {
        btntext = '暂停';
    } else {
        btntext = 'Pause';
    }
    if ($("#but_prt").text() == btntext) {
        if (lang == 'zh') {
            btnnewtext = '继续';
        } else {
            btnnewtext = 'Continue';
        }
        $.get('./pause', function (data) {
            if (data == "ok") {
                $("#but_prt").text(btnnewtext);
                if (lang == 'zh') {
                    msg = '暂停成功!';
                } else {
                    msg = 'success !';
                }
                $.notify({
                    message: msg,
                    status: 'success'
                });
            }
            else {
                if (lang == 'zh') {
                    msg = '暂停失败!';
                } else {
                    msg = 'fail !';
                }
                $.notify({
                    message: msg,
                    status: 'warning'
                });
            }
        });
    }
    else {
        $.get('./resume', function (data) {
            if (lang == 'zh') {
                btnnewtext = '暂停';
            } else {
                btnnewtext = 'Pause';
            }
            if (data == "ok") {
                if (lang == 'zh') {
                    msg = '继续成功!';
                } else {
                    msg = 'success !';
                }
                $("#but_prt").text(btnnewtext);
                $.notify({
                    message: msg,
                    status: 'success'
                });
            }
            else {
                if (lang == 'zh') {
                    msg = '继续失败!';
                } else {
                    msg = 'fail !';
                }
                $.notify({
                    message: msg,
                    status: 'warning'
                });
            }
        });
    }
});
$('#but_stop').click(function () {//强制停止打印文件
    cancelPrint();
});
$('#bs_stp').click(function () {//强制停止打印文件
    forceStop();
});

function cancelPrint(){
    $.get('./cancel', function (data) {
        if (data == "ok") {
            if (lang == 'zh') {
                msg = '取消成功!';
            } else {
                msg = 'success !';
            }
            $.notify({
                message: msg,
                status: 'success'
            });
            $("#filetable").show();
            $("#mac_ctrl").show();
            $("#info_status").hide();
        }
        else {
            if (lang == 'zh') {
                msg = '取消失败!';
            } else {
                msg = 'fail !';
            }
            $.notify({
                message: msg,
                status: 'warning'
            });
        }
    });
}

function forceStop() {
    $.get('./reset', function (data) {
        if (data == "ok") {
            if (lang == 'zh') {
                msg = '强制停止成功!';
            } else {
                msg = 'success !';
            }
            $.notify({
                message: msg,
                status: 'success'
            });
            $("#filetable").show();
            $("#mac_ctrl").show();
            $("#info_status").hide();
        }
        else {
            if (lang == 'zh') {
                msg = '强制停止失败!';
            } else {
                msg = 'fail !';
            }
            $.notify({
                message: msg,
                status: 'warning'
            });
        }
    });
}