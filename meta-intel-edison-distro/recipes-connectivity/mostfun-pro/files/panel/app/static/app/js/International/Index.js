/**
 * Created by Administrator on 2015/8/6.
 */
// 首页
(function ($, window, document) {
    $(document).ready(function () {
        jQuery.i18n.properties({
            name: 'strings', //资源文件名称
            path: 'static/app/js/International/i18n/', //资源文件路径
            mode: 'map', //用Map的方式使用资源文件中的值
            language: lang,
            callback: function () {//加载成功后设置显示内容
                $('title').text($.i18n.prop('tlt_index'));
                $('#deg_info').text($.i18n.prop('deg_info'));
                $('#con_panel').text($.i18n.prop('con_panel'));
                $('#Noz_heat').text($.i18n.prop('Noz_heat'));
                $('#bed_heat').text($.i18n.prop('bed_heat'));
                $('#Send').text($.i18n.prop('Send'));
                $('#Rel_coor').text($.i18n.prop('Rel_coor'));
                $('#xy_spo').text($.i18n.prop('xy_spo'));
                $('#z_spo').text($.i18n.prop('z_spo'));
                $('#Ext_heat').text($.i18n.prop('Ext_heat'));
                $('#Ext_spo').text($.i18n.prop('Ext_spo'));
                $('#pri_info').text($.i18n.prop('pri_info'));
                $('#info_ptrname').text($.i18n.prop('info_ptrname'));
                $('#info_layecount').text($.i18n.prop('info_layecount'));
                $('#info_layenow').text($.i18n.prop('info_layenow'));
                $('#info_layeper').text($.i18n.prop('info_layeper'));
                $('#time_left').text($.i18n.prop('time_left'));
                $('#info_e0temp').text($.i18n.prop('info_e0temp'));
                $('#info_bedtemp').text($.i18n.prop('info_bedtemp'));
                $('#but_prt').text($.i18n.prop('but_prt'));
                $('#but_stop').text($.i18n.prop('but_stop'));
                $('#myModal h4').text($.i18n.prop('myModal'));
                $('#close').text($.i18n.prop('close'));
                $('#webcam h4').text($.i18n.prop('came'));
                $('#wreplace h4').text($.i18n.prop('Refl'));
                $('#Refl').text($.i18n.prop('Refl'));
                $('#Noz_cen').text($.i18n.prop('Noz_cen'));
                $('#Noz_hea').text($.i18n.prop('Noz_hea'));
                $('#ctl_z').text($.i18n.prop('ctl_z'));
                $('#ctl_E').text($.i18n.prop('ctl_E'));
            }
        });
    });
}(jQuery, window, document));