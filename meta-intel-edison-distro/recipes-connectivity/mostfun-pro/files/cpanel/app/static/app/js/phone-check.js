/**
 * Created by Jux.Liu on 2015/8/13.
 */
var phone = false;
function checkPlatform() {
    if (/android/i.test(navigator.userAgent)) {
        //document.write("This is Android'browser.");//����Androidƽ̨�������
        phone = true;
    }
    if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
        //document.write("This is iOS'browser.");//����iOSƽ̨�������
        phone = true;
    }
    //if(/Linux/i.test(navigator.userAgent)){
    //	document.write("This is Linux'browser.");//����Linuxƽ̨�������
    //}
    //if(/Linux/i.test(navigator.platform)){
    //	document.write("This is Linux operating system.");//����Linux����ϵͳƽ̨
    //}
    if (/MicroMessenger/i.test(navigator.userAgent)) {
        //document.write("This is MicroMessenger'browser.");//����΢��ƽ̨�������
        phone = true;
    }
}

$(document).ready(function () {
    checkPlatform();
});