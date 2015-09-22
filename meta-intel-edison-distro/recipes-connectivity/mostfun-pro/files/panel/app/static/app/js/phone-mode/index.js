/**
 * Created by Administrator on 2015/8/11.
 */
//手机端判断各个平台浏览器及操作系统平台
(function ($, window, document) {
    $(document).ready(function () {
        if (phone) {
            $('#tmp_info').hide();
            $('#ctl_pnl').hide();
            // todo: test status. if it's ok
            if (status == 'ready') {
                $("#info_status_div").hide();
                $("#info_status_").hide();
            } else {
                $("#info_status_div").show();
                $("#info_status_").show();
            }
            tem.style.display = "";
        }
        else {
            $('#tmp_info').show();
            $('#ctl_pnl').show();
            $("#tem").hide();
        }
    });
}(jQuery, window, document));
