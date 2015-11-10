/**
 * Created by Administrator on 2015/8/10.
 */
// 文件管理界面
(function ($, window, document) {
    $(document).ready(function () {
        jQuery.i18n.properties({
            name: 'strings', //资源文件名称
            path: 'static/app/js/International/i18n/', //资源文件路径
            mode: 'map', //用Map的方式使用资源文件中的值
            language : lang,
            callback: function () {//加载成功后设置显示内容
                $('title').text($.i18n.prop('tlt_mag'));
                $('#dragtext').text($.i18n.prop('dragtext'));
                $('#choose').text($.i18n.prop('choose'));
                $('#filemanege').text($.i18n.prop('filemanege'));
                $('#filename').text($.i18n.prop('filename'));
                $('#description').text($.i18n.prop('description'));
                $('#large').text($.i18n.prop('large'));
                $('#myModal h4').text($.i18n.prop('myModal'));
                $('#webcam h4').text($.i18n.prop('came'));
                $('#newtime').text($.i18n.prop('newtime'));
                $('#print').text($.i18n.prop('print'));
                $('#close').text($.i18n.prop('close'));
                $('#Delete').text($.i18n.prop('Delete'));
                $('#Export').text($.i18n.prop('Export'));
                $('#remove').text($.i18n.prop('remove'));
            }
        });
    });
}(jQuery, window, document));