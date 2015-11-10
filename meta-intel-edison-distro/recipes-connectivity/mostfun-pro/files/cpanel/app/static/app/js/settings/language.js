/**
 * Created by Jux.Liu on 2015/8/14.
 */

$(document).ready(function () {
    $("#lang_save").click(function () {
        changeLang($('input:radio[name="language"]:checked').val());
    });
});
