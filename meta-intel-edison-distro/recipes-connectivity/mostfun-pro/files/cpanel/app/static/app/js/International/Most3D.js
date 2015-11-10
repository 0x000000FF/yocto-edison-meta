/**
 * Created by Administrator on 2015/8/7.
 */
//获取模型界面
(function ($, window, document) {
    $(document).ready(function () {
        jQuery.i18n.properties({
            name: 'strings', //资源文件名称
            path: 'static/app/js/International/i18n/', //资源文件路径
            mode: 'map', //用Map的方式使用资源文件中的值
            language : lang,
            callback: function () {//加载成功后设置显示内容
                //获取模型
                $('title').text($.i18n.prop('tlt_most3d'));
                $('#gt').text($.i18n.prop('gt'));
                $('#3dvi').text($.i18n.prop('3dvi'));
                $('#sta').text($.i18n.prop('sta'));
                $('#3dvol h4').text($.i18n.prop('myModal'));
                $('#close').text($.i18n.prop('close'));
                //搜索框界面
                $('#param').attr('placeholder', $.i18n.prop('search'));
                $('#search').text($.i18n.prop('search'));
                $('#dat_tie').text($.i18n.prop('dat_tie'));
                $('#aut_nam').text($.i18n.prop('aut_nam'));
            }
        });
    });
}(jQuery, window, document));