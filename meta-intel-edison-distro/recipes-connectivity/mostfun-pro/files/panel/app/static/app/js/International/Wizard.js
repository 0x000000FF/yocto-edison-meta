/**
 * Created by Administrator on 2015/8/7.
 */
/**
 * Created by Administrator on 2015/8/6.
 */
//向导界面
(function ($, window, document) {
    $(document).ready(function () {
        jQuery.i18n.properties({
            name: 'strings', //资源文件名称
            path: 'static/app/js/International/i18n/', //资源文件路径
            mode: 'map', //用Map的方式使用资源文件中的值
            language : lang,
            callback: function () {//加载成功后设置显示内容
                $('title').text($.i18n.prop('tlt_wizard'));
                $('#Refl').text($.i18n.prop('Refl'));
                $('#Rea_refl').text($.i18n.prop('Rea_refl'));
                $('#Empty').text($.i18n.prop('Empty'));
                $('#Mob_heat').text($.i18n.prop('Mob_heat'));
                $('#Tak_out').text($.i18n.prop('Tak_out'));
                $('#Feed').text($.i18n.prop('Feed'));
                $('#Insert').text($.i18n.prop('Insert'));
                $('#Tes_ext').text($.i18n.prop('Tes_ext'));
                $('#Obser').text($.i18n.prop('Obser'));
                $('#rep').text($.i18n.prop('rep'));
                $('#stgh').text($.i18n.prop('stgh'));
                $('#clik').text($.i18n.prop('clik'));
                $('#tet').text($.i18n.prop('tet'));
                $('#Ext').text($.i18n.prop('Ext'));
                $('#Comp').text($.i18n.prop('Comp'));
                $('#Noz_cen').text($.i18n.prop('Noz_cen'));
                $('#Noz_hea').text($.i18n.prop('Noz_hea'));
            }
        });
    });
}(jQuery, window, document));