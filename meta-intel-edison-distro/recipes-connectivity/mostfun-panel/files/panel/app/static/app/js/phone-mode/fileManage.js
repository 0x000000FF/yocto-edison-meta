/**
 * Created by OJ on 2015/9/24.
 */

//手机端判断各个平台浏览器及操作系统平台
(function ($, window, document) {
    $(document).ready(function () {
        if (phone) {
            $('#fileManage-file').hide();
        }
    });
}(jQuery, window, document));
