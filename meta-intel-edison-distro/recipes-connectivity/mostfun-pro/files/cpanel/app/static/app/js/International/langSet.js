/**
 * Created by Jux.Liu on 2015/8/14.
 */
var lang = '';

function changeLang(tarLang) {
    $.ajax({
        url: '/setLang',
        data: {lang: tarLang},
        type: "POST",
        dataType: 'json',
        success: function (data) {
            if (data['result']) {
                window.location.reload();
            }
        }
    });
}

$(document).ready(function () {
    $.ajax({
        url: '/getLang',
        data: {},
        type: 'GET',
        timeout: 50000,
        dataType: 'json',
        async: false,
        success: function (data) {
            if (data['lang'].length > 0) {
                lang = data['lang'];
            }
            else
            {
                lang = $.i18n.browserLang();
            }
        },
        error: function () {
            lang = $.i18n.browserLang();
        }
    });
});