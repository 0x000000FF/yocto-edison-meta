/**
 * Created by Administrator on 2015/8/10.
 */
// 使用帮助页
(function ($, window, document) {
    $(document).ready(function () {
        jQuery.i18n.properties({
            name: 'strings', //资源文件名称
            path: 'static/app/js/International/i18n/', //资源文件路径
            mode: 'map', //用Map的方式使用资源文件中的值
            language: lang,
            callback: function () {//加载成功后设置显示内容
                $('#webcam h4').text($.i18n.prop('came'));
                $('#came').text($.i18n.prop('came'));
                $('#close_cam').text($.i18n.prop('close'));
                $('#stp').text($.i18n.prop('stp'));
                $('#tlt_index').text($.i18n.prop('tlt_index'));
                $('#tlt_mag').text($.i18n.prop('tlt_mag'));
                $('#most3d').text($.i18n.prop('most3d'));
                $('#set').text($.i18n.prop('set'));
                $('#user_gud').text($.i18n.prop('user_gud'));
                $('#tlt_help').text($.i18n.prop('tlt_help'));
                $('#tlt_getApp').text($.i18n.prop('tlt_getApp'));
                $('#fl_china').text($.i18n.prop('fl_china'));
                $('#fl_item').text($.i18n.prop('fl_item'));
                $('#title_index').attr("title", $.i18n.prop('tlt_index'));
                $('#title_fielMg').attr("title", $.i18n.prop('tlt_mag'));
                $('#title_getmodel').attr("title", $.i18n.prop('most3d'));
                $('#title_set').attr("title", $.i18n.prop('set'));
                $('#title_guide').attr("title", $.i18n.prop('tlt_wizard'));
                $('#title_help').attr("title", $.i18n.prop('tlt_help'));
                $('#title_getapp').attr("title", $.i18n.prop('tlt_getApp'));

            }
        });
    });
}(jQuery, window, document));