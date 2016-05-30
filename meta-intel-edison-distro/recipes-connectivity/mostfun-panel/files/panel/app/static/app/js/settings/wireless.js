/**
 * Created by Jux.Liu on 2015/5/28.
 */


(function ($, window, document) {

    $("#wifi_refresh").click(function () {
        refresh_list();
    });

    function refresh_list() {
        $.ajax({
            url: '/get-wireless-list',
            data: {},
            type: "GET",//请求方式
            timeout: 20000,//超时时间
            dataType: 'json',
            beforeSend: function (event) {//前置事件
            },
            success: function (_data) {
                /*成功响应返回值*/
                var html = '';
                console.log(_data);
                if (_data.length != 0) {
                    var no = 1;
                    for (var item in _data) {
                        db = 100 - Math.abs(_data[item]['db']);
                        dbc = '';
                        if (db < 25) {
                            dbc = "progress-bar-danger";
                        } else if (db >= 26 && db < 50) {
                            dbc = "progress-bar-info";
                        } else {
                            dbc = "progress-bar-success";
                        }
                        html += '<tr><td>' + no + '</td><td>' + decodeX(_data[item]['ssid']) +
                            '</td><td><div class="progress progress-striped progress-xs"><div class="progress-bar ' + dbc +
                            '" style="width: ' + db +
                            '%;"aria-valuemax="80" aria-valuemin="0" aria-valuenow="20" role="progressbar">' +
                            '<span class="sr-only">' + db +
                            '% Complete</span></div></div></td><td>' + _data[item]['secure'] +
                            '</td><td><div><button class="btn btn-primary connect" type="button" name="connect" sec-toggle="' +
                            _data[item] + '" ssid-toggle="' + item + '" id="' + no + '"></button></div>\
    </td>\
</tr>';
                        no++;
                    }
                } else {
                    html = '<tr><td></td><td></td><td id="no_conn"></td><td></td><td></td></tr>';
                }
                $("#wifi_list").html(html).ajaxStop(
                    jQuery.i18n.properties({
                        name: 'strings', //资源文件名称
                        path: 'static/app/js/International/i18n/', //资源文件路径
                        mode: 'map', //用Map的方式使用资源文件中的值
                        language: lang,
                        callback: function () {//加载成功后设置显示内容
                            //无线设置
                            $('.connect').text($.i18n.prop('connect'));
                        }
                    }));
            },
            error: function () {//错误或者超时
                $("#wifi_list").html('<tr><td></td><td></td><td id="no_conn"></td><td></td><td></td></tr>');
            },
            complete: function () {//完成请求
                $('#wifi_list_panel').attr('class', 'panel panel-primary');
            }
        });
    }

    $(document).on('click', 'button[name="connect"]', function () {
        if ($(this).attr('sec-toggle').toLowerCase() == 'open') {
            $('#wifi_password').hide();
            connect_wifi($(this).attr('ssid-toggle'), '');
        } else {
            $('#wifi_password').show();
            $("#ssid").val($(this).attr('ssid-toggle'));
        }
    });

    $('#connect').click(function () {
        var ssid = $('#ssid').val();
        var password = $('#wifi-password').val();
        if (ssid.length > 0 & password.length > 8) {
            connect_wifi(ssid, password);
        }
    });

    function connect_wifi(ssid, password) {
        $.ajax({
            url: '/connect-wifi',
            data: {
                ssid: ssid,
                password: password
            },
            type: "POST",
            dataType: 'json',
            success: function (data) {
                //alert(_data);
            }
        });
    }

    $("#get_current_wifi").click(function () {
        getCurrWifi();
    });

    function getCurrWifi() {
        $.ajax({
            url: '/get-current-wifi',
            data: {},
            type: "POST",
            dataType: 'json',
            success: function (data) {
                $("#curr_wifi_ssid").text(data['ssid']);
                $('#current_wifi_panel').attr('class', 'panel panel-primary');
            }
        });
    }


    $('#AP_set').click(function () {
        alert('AP_set');
        var ssid = $('#AP_ssid').val();
        var password = $('#AP_password').val();
        if (ssid.length > 0 || password.length >= 8) {
            set_ap(ssid, password);
        }
    });

    function set_ap(ssid, password) {
        $.ajax({
            url: '/config_wpa',
            data: {
                ssid: ssid,
                password: password
            },
            type: "POST",
            dataType: 'json',
            success: function (data) {
                var msg = '';
                if (!data['result']) {
                    msg = data['msg'];
                } else {
                    if (lang == "zh") {
                        msg = '设置成功！';
                    }
                    else {
                        msg = 'Success !';
                    }
                }
                alert(msg);
            }
        });
    }

    function decodeX(s) {
        var temp = s.toLowerCase();
        if (temp.indexOf("\\x")) {
            return s;
        }
        var res = decodeURI(s.replace(/\\x/g, '%'));
        return res;
    }

    getCurrWifi();

}(jQuery, window, document));
