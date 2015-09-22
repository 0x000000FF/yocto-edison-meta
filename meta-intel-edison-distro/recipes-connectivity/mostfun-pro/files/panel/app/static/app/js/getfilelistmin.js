// JavaScript source code
var view_id;
function getfilelistmin() {
    $.getJSON('./get/filelist', function (json) {
        if (json.length > 0) {
            for (var i = 0; i < json.length; i++) {
                json[i].push("");
                json[i].unshift("");
            }
            for (i = 0; i < json.length; i++) {
                json[i][0] = "<div class=\"checkbox c-checkbox\"><label><input type=\"checkbox\"><span class=\"fa fa-check\"></span></label></div>";
                json[i][3] = json[i][3] + 'MB';
                //json[i][5] = "<button onclick=\"prt(" + i + ")\" type=\"button\" class=\"btn btn-default trp\"></button>";
                json[i][5] = "<button data-toggle=\"modal\" data-target=\"#myModal\" class=\"btn-view3d btn btn-default\" onclick=\"view(" + i + ")\"></button>";
                if (!phone) {
                    json[i][5] = "<div class=\"btn-group\">" + json[i][5] +
                        "<button style=\"height: 38px;\" type=\"button\" data-toggle=\"dropdown\" class=\"btn btn-default dropdown-toggle trp-more\">" +
                        "<span class=\"caret\"></span>" +
                        "</button>" +
                        "<ul role=\"menu\" class=\"dropdown-menu\">" +
                        //"<li><a href=\"#\" data-toggle=\"modal\" data-target=\"#myModal\" class=\"btn-view3d\" onclick=\"view(" + i + ")\"></a></li>" +
                        "<li><a href=\"#\" class= \"btn-edit\" ></a></li><li class=\"divider\"></li>" +
                        "<li><a href=\"#\" class=\"btn-delete\" onclick=\"del(" + i + ")\"></a></li></ul></div>";
                }
            }

            $('#example').dataTable().fnDestroy();
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
                    {"sTitle": "<div data-toggle=\"tooltip\" data-title=\"Check All\" class=\"checkbox c-checkbox\"><label><input type=\"checkbox\"><span class=\"fa fa-check\"></span></label></div>"},
                    {"sClass": "center", "sStyle": "width: 100px;"},
                    {"sClass": "center hidden-xs"},
                    {"sClass": "hidden-xs"},
                    {"sClass": "center hidden-xs", "": ""},
                    {
                        "sClass": "center"
                    }
                ],
                data: json
            });

            $('#buttondel').click(function () {//删除文件
                var filename = './del/' + table.cell('.selected', 1).data();
                //alert(table.cell('.selected', 0).data());
                //alert(filename);
                $.get(filename, function (data) {
                    if (data == "ok") {
                        if (lang = "zh") {
                            msg = "删除成功 !";
                        }
                        else {
                            msg = "Delete success !";
                        }
                        $.notify({
                            message: msg,
                            status: 'success'
                        });
                        table.row('.selected').remove().draw(false);
                    }
                    else {
                        if (lang = "zh") {
                            msg = "删除失败 !";
                        }
                        else {
                            msg = "Delete fail !";
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
                        if (lang = "zh") {
                            msg = "开始打印 !";
                        }
                        else {
                            msg = "Printing !";
                        }
                        $.notify({
                            message: msg,
                            status: 'success'
                        });
                    }
                    else {
                        if (lang = "zh") {
                            msg = "打印失败 !";
                        }
                        else {
                            msg = "Printing fail ! ";
                        }
                        $.notify({
                            message: msg,
                            status: 'warning'
                        });
                    }
                });
            });
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
        }
    });
};

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
            if (lang = "zh") {
                msg = "打印失败 !";
            }
            else {
                msg = "Printing fail ! ";
            }
            $.notify({
                message: msg,
                status: 'warning',
            });
        }
    });
};

function view(id) {//查看文件
    var table = $('#example').DataTable();
    view_id = id;
};

function del(id) {//删除文件
    var table = $('#example').DataTable();
    $.get('./del/' + table.cell(id, 1).data(), function (data) {
        if (data == "ok") {
            if (lang = "zh") {
                msg = "删除成功 !";
            }
            else {
                msg = "Delete success !";
            }
            $.notify({
                message: msg,
                status: 'success',
            });
            table.row(id).remove().draw(false);
        }
        else {
            if (lang = "zh") {
                msg = "删除失败 !";
            }
            else {
                msg = "Delete fail !";
            }
            $.notify({
                message: msg,
                status: 'warning',
            });
        }
    });
};


function selectAll() {
    var objs = document.getElementsByTagName("input");
    for (var i = 0; i < objs.length; i++) {
        var obj = objs[i];
        if (obj.type == "checkbox") {
            if (i != 0) {
                if (obj.checked) {
                    obj.checked = false;
                } else {
                    obj.checked = true;
                }
            }
        }
    }
};


var filename_list = "";
$("#remove").click(function () {
    $("table tr").each(function () {
        if ($(this).children('td').eq(0).find("input:checkbox").prop("checked")) {
            // alert($(this).children('td').eq(1).html());
            filename_list += $(this).children('td').eq(1).html() + ",";
        }
    });
    $.post('./dels', {data: filename_list}, function (data) {
        if (data == "ok") {
            if (lang = "zh") {
                msg = "删除成功 !";
            }
            else {
                msg = "Delete success !";
            }
            $.notify({
                message: msg,
                status: 'success',
            });
            var start = $("#example").dataTable().fnSettings()._iDisplayStart;
            var total = $("#example").dataTable().fnSettings().fnRecordsDisplay();
            window.location.reload();
            if ((total - start) == 1) {
                if (start > 0) {
                    $("#example").dataTable().fnPageChange('previous', true);
                }
            }
            //  $("input:checked").parents("tr").remove();
        }
        else {
            if (lang = "zh") {
                msg = "删除失败 !";
            }
            else {
                msg = "Delete fail !";
            }
            $.notify({
                message: msg,
                status: 'warning',
            });
        }
    });
});

$('#myModal').on('show.bs.modal', function () {
    var table = $('#example').DataTable();
    document.getElementById("myframe").src = '3dv/' + table.cell(view_id, 1).data().replace(".gcode", ".stl");
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
