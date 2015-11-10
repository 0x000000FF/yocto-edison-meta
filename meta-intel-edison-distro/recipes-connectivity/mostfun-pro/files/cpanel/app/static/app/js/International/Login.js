/**
 * Created by Administrator on 2015/8/7.
 */
//登录界面
(function ($, window, document) {
    $(document).ready(function () {

        $('#lang_en').click(function () {
            changeLang('en');
        });
        $('#lang_zh').click(function () {
            changeLang('zh')
        });

        jQuery.i18n.properties({
            name: 'strings', //资源文件名称
            path: 'static/app/js/International/i18n/', //资源文件路径
            mode: 'map', //用Map的方式使用资源文件中的值
            language: lang,
            callback: function () {//加载成功后设置显示内容
                $('#Lgn').text($.i18n.prop('Lgn'));
                $('#Ini_pwd').text($.i18n.prop('Ini_pwd'));
                $('#came').text($.i18n.prop('came'));
                $('#webcam h4').text($.i18n.prop('came'));
                $('#close').text($.i18n.prop('close'));
                $('.checkbox label').html('<input type="checkbox" value="y" name="remember_me" id="remember_me">' + $.i18n.prop('remember_me'));
                $('#submit').val($.i18n.prop('submit'));
                $('#Pasd').val($.i18n.prop('Pasd'));
                $('#fl_china').text($.i18n.prop('fl_china'));
                $('#fl_item').text($.i18n.prop('fl_item'));
                $('#err_msg').text($.i18n.prop('err_msg'));
            }
        });
    });
}(jQuery, window, document));