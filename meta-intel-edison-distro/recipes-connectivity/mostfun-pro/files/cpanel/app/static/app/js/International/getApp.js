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
            language : lang,
            callback: function () {//加载成功后设置显示内容
                //获取app;
                $('title').text($.i18n.prop('tlt_getApp'));
                $('#QR_code').text($.i18n.prop('QR_code'))
            }
        });
    });
}(jQuery, window, document));