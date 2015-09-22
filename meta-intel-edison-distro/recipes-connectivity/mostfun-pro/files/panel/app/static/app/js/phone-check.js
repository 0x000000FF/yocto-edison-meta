/**
 * Created by Jux.Liu on 2015/8/13.
 */
var phone = false;
function checkPlatform() {
    if (/android/i.test(navigator.userAgent)) {
        //document.write("This is Android'browser.");//这是Android平台下浏览器
        phone = true;
    }
    if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
        //document.write("This is iOS'browser.");//这是iOS平台下浏览器
        phone = true;
    }
    //if(/Linux/i.test(navigator.userAgent)){
    //	document.write("This is Linux'browser.");//这是Linux平台下浏览器
    //}
    //if(/Linux/i.test(navigator.platform)){
    //	document.write("This is Linux operating system.");//这是Linux操作系统平台
    //}
    if (/MicroMessenger/i.test(navigator.userAgent)) {
        //document.write("This is MicroMessenger'browser.");//这是微信平台下浏览器
        phone = true;
    }
}

$(document).ready(function () {
    checkPlatform();
});