/**
 * Created by Administrator on 2015/8/3.
 */
//设置页、App页、帮助页
(function ($, window, document) {
    $(document).ready(function () {
        jQuery.i18n.properties({
            name: 'strings', //资源文件名称
            path: 'static/app/js/International/i18n/', //资源文件路径
            mode: 'map', //用Map的方式使用资源文件中的值
            language : lang,
            callback: function () {//加载成功后设置显示内容
                //MostFun设置
                $('title').text($.i18n.prop('tlt_setting'));
                $('#MFset').text($.i18n.prop('MFset'));
                $('#Pwd').text($.i18n.prop('Pwd'));
                $('#firm').text($.i18n.prop('firm'));
                $('#email').text($.i18n.prop('email'));
                $('#wire').text($.i18n.prop('wire'));
                $('#lang').text($.i18n.prop('language'));
                //密码设置
                $('#oldPwd').text($.i18n.prop('oldPwd'));
                $('#newPwd').text($.i18n.prop('newPwd'));
                $('#copyPwd').text($.i18n.prop('copyPwd'));
                $('#save').text($.i18n.prop('save'));
                //固件设置
                $('#cut_cp_ven').text($.i18n.prop('cut_cp_ven'));
                $('#cut_sys_ven').text($.i18n.prop('cut_sys_ven'));
                $('#update_cp_frimware').text($.i18n.prop('update_cp_frimware'));
                $('#update_sys_frimware').text($.i18n.prop('update_sys_frimware'));
                $('#chkCPOnline').text($.i18n.prop('chkCPOnline'));
                $('#chkSYSOnline').text($.i18n.prop('chkSYSOnline'));
                $('#update_start').text($.i18n.prop('update_start'));
                //邮件设置
                $('#mah_mail').text($.i18n.prop('mah_mail'));
                $('#MailPassword').text($.i18n.prop('MailPassword'));
                $('#Mailserver').text($.i18n.prop('Mailserver'));
                $('#ServerPort').text($.i18n.prop('ServerPort'));
                $('#TitlePrefix').text($.i18n.prop('TitlePrefix'));
                $('#SenderName').text($.i18n.prop('SenderName'));
                $('#ReceiveMail').text($.i18n.prop('ReceiveMail'));
                $('#sure').text($.i18n.prop('sure'));
                //无线设置
                $('#Cur_connect').text($.i18n.prop('Cur_connect'));
                $('#AP_setting').text($.i18n.prop('AP_setting'));
                $('#curr_wifi_info').text($.i18n.prop('curr_wifi_info'));
                $('#Wil_det').text($.i18n.prop('Wil_det'));
                $('#name').text($.i18n.prop('name'));
                $('#Signal').text($.i18n.prop('Signal'));
                $('#method').text($.i18n.prop('method'));
                $('#EnterPassword').text($.i18n.prop('EnterPassword'));
                $('#cont_name').text($.i18n.prop('cont_name'));
                $('#cont_password').text($.i18n.prop('cont_password'));
                $('#connect').text($.i18n.prop('connect'));
                $('#AP_set').text($.i18n.prop('AP_set'));
                $('#AP_name').text($.i18n.prop('AP_name'));
                $('#AP_passwd').text($.i18n.prop('AP_passwd'));
                $('#no_conn').text($.i18n.prop('no_conn'));
                //语言设置
                $('#lang_save').text($.i18n.prop('save'));
            }
        });
    });
}(jQuery, window, document));