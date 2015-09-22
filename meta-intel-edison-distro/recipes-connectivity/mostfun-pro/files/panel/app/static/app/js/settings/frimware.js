/**
 * Created by Jux.Liu on 2015/5/27.
 */

/**
 * Upload frimware file.
 */
(function ($, window, document) {
    $('.btn').click(function () {
        var btnid = $(this).attr('id');
        var chkurl = '';
        var dataurl = '';
        if (btnid == 'chkCPOnline') {
            chkurl = '/chk-cp-update';
            dataurl = '/update-cp';
        } else if (btnid == 'chkSYSOnline') {
            chkurl = '/chk-sys-update';
            dataurl = '/update-sys';
        } else {
            return;
        }
        $('#up_btn').css('display', 'none');
        $.get(chkurl, function (_data) {
            _data = JSON.parse(_data);
            if (_data['result']) {
                $('#update_start').attr('data-url', dataurl);
                $('#up_btn').css('display', 'block');
            } else {
                alert(_data['msg']);
            }
        });
    });

    $('#update_start').click(function () {
        $.ajax({
            url: $(this).attr("data-url"),
            type: 'POST',
            timeout: 150000,
            error: function () {
                location.href = "logout";
            }
        });
    });

}(jQuery, window, document));
