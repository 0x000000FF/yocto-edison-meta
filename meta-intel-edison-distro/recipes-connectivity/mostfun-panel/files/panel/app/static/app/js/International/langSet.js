/**
 * Created by Jux.Liu on 2015/8/14.
 */
var lang = '';

function changeLang(tarLang) {
	
	localStorage.setItem('locale', tarLang);
	lang = tarLang;
	
    $.ajax({
        url: '/setLang/',
        data: JSON.stringify({lang: tarLang}),
        type: "POST",
        dataType: 'json',
		contentType: 'application/json;charset=utf-8',
        success: function (data) {
            window.location.reload();
        }
    });
}

function getLang(){
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
                lang = navigator.language.toLowerCase();
            }
        },
        error: function () {
            lang = navigator.language.toLowerCase();
        }
    });
}

$(document).ready(getLang());