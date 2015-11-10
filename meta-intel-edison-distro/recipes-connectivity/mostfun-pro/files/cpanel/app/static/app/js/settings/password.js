/**
 * Created by Jux.Liu on 2015/6/1.
 */

(function ($, window, document) {

    $('#change_password_form').submit(function () {
        // 提取对象
        old_password = $('#old_password');
        new_password = $('#new_password');
        rpt_password = $('#rpt_password');
        old_password_p = old_password.parent();
        new_password_p = new_password.parent();
        rpt_password_p = rpt_password.parent();

        // 重置样式
        new_password_p.removeClass('has-error');
        rpt_password_p.removeClass('has-error');
        old_password_p.removeClass('has-error');
        $('#change_password_msg').text('');

        if (!check_repass(new_password, rpt_password)) {     // 判断新密码与重复密码是否匹配
            // 错误信息
            new_password_p.addClass('has-error');
            rpt_password_p.addClass('has-error');
            $('#change_password_msg').show().text('两次输入的密码不匹配');
            return false;
        }
    });

    function check_repass(ele_1, ele_2) {
        return ele_1.val() == ele_2.val();
    }

}(jQuery, window, document));
