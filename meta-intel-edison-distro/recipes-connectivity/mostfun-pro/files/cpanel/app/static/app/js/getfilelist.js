// JavaScript source code
var view_id;
function getfilelist() {
    $.getJSON('./get/filelist', function (json) {
        for (var i = 0; i < json.length; i++) {
            json[i].push("");
        }
        for (i = 0; i < json.length; i++) {
            json[i][2] = json[i][2] + 'MB';
            json[i][4] = "<button onclick=\"prt(" + i + ")\" type=\"button\" class=\"btn btn-default trp\"></button>";

            if (!phone) {
                json[i][4] = "<div class=\"btn-group\">" + json[i][4] +
                    "<button style=\"height: 38px;\" type=\"button\" data-toggle=\"dropdown\" class=\"btn btn-default dropdown-toggle\">" +
                    "<span class=\"caret\"></span>" +
                    "</button>" +
                    "<ul role=\"menu\" class=\"dropdown-menu\">" +
                    "<li><a href=\"#\" data-toggle=\"modal\" data-target=\"#myModal\" class=\"btn-view3d\" onclick=\"view(" + i + ")\"></a></li>" +
                    "<li><a href=\"#\" class= \"btn-edit\" ></a></li>" +
                    "<li class=\"divider\"></li>" +
                    "<li><a href=\"#\" class=\"btn-delete\" onclick=\"del(" + i + ")\"></a></li></ul></div>";
            }
        }
        $('#example').DataTable({
            "asStripClasses": [],
            //"columns": [
            //    { "width": "100px"},
            //    {"width"：},
            //    null,
            //    null,
            //    { "width": "100px" },
            //],
            "aoColumns": [
                {"sClass": "center", "sStyle": "width: 100px;"},
                {"sClass": "center hidden-xs"},
                {"sClass": ""},
                {"sClass": "center hidden-xs", "": ""},
                {
                    "sClass": "center",
                }
            ],
            data: json
        });
        $('#buttondel').click(function () {//删除文件
            var filename = './del/' + table.cell('.selected', 0).data();
            //alert(table.cell('.selected', 0).data());
            //alert(filename);
            $.get(filename, function (data) {
                if (data == "ok") {
                    if (lang == 'zh') {
                        msg = '删除成功 !';
                    } else {
                        msg = 'success !';
                    }
                    $.notify({
                        message: msg,
                        status: 'success'
                    });
                    table.row('.selected').remove().draw(false);
                }
                else {
                    if (lang == 'zh') {
                        msg = '删除失败 !';
                    } else {
                        msg = 'fail !';
                    }
                    $.notify({
                        message: msg,
                        status: 'warning'
                    });
                }
            });

        });
        $('#buttonprt').click(function () {//打印文件
            //alert(table.cell('.selected', 0).data());
            $.get('./print/' + table.cell('.selected', 0).data(), function (data) {
                if (data == "ok") {
                    if (lang == 'zh') {
                        msg = '开始打印 !';
                    } else {
                        msg = 'start printing !';
                    }
                    $.notify({
                        message: msg,
                        status: 'success'
                    });
                }
                else {
                    if (lang == 'zh') {
                        msg = '打印失败 !';
                    } else {
                        msg = 'fail !';
                    }
                    $.notify({
                        message: msg,
                        status: 'warning'
                    });
                }
            });
        });

        setTimeout(function () {
            $('#filetable').ajaxStop(
                jQuery.i18n.properties({
                    name: 'strings', //资源文件名称
                    path: 'static/app/js/International/i18n/', //资源文件路径
                    mode: 'map', //用Map的方式使用资源文件中的值
                    language: lang,
                    callback: function () {//加载成功后设置显示内容
                        $('#fil_mag').text($.i18n.prop('fil_mag'));
                        $('#fil_nam').text($.i18n.prop('fil_nam'));
                        $('#desp').text($.i18n.prop('desp'));
                        $('#lar_sml').text($.i18n.prop('lar_sml'));
                        $('#new_tim').text($.i18n.prop('new_tim'));
                        $('#pri').text($.i18n.prop('pri'));
                        $('.trp').text($.i18n.prop('print'));
                        $('.btn-view3d').text($.i18n.prop('btn_view3d'));
                        $('.btn-edit').text($.i18n.prop('btn_edit'));
                        $('.btn-delete').text($.i18n.prop('btn_delete'));
                    }
                })
            );
        }, 10);
    })
}

function prt(id) {//打印文件
    var table = $('#example').DataTable();
    $.get('./print/' + table.cell(id, 0).data(), function (data) {
        if (data == "ok") {
            //$.notify({
            //    message: '开始打印!',
            //    status: 'success',
            //});
            getstatus();
        }
        else {
            if (lang == 'zh') {
                msg = '打印失败 !';
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

function view(id) {//查看文件
    var table = $('#example').DataTable();
    view_id = id;
}

function del(id) {//删除文件
    var table = $('#example').DataTable();
    $.get('./del/' + table.cell(id, 0).data(), function (data) {
        if (data == "ok") {
            if (lang == 'zh') {
                msg = '删除成功 !';
            } else {
                msg = 'success !';
            }
            $.notify({
                message: msg,
                status: 'success'
            });
            table.row(id).remove().draw(false);
        }
        else {
            if (lang == 'zh') {
                msg = '删除失败 !';
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

$('#myModal').on('show.bs.modal', function () {
    var table = $('#example').DataTable();
    document.getElementById("myframe").src = '3dv/' + table.cell(view_id, 0).data().replace(".gcode", ".stl");
    $(function () {
        $('#filetable').collapse('hide')
    });
})

$("#myModal").on("hidden.bs.modal", function () {
    $(this).removeData("bs.modal");
    $(function () {
        $('#filetable').collapse('show')
    });
});
