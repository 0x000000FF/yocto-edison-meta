/**
 * Created by Jux.Liu on 2015/9/10.
 */
$(document).ready(function () {
    $('#webcam').on('show.bs.modal', function () {
        //document.getElementById("cam_img").src = window.location.hostname + ':8080/?action=stream';
        document.getElementById("camframe").src = "http://" + window.location.hostname + '/webcam';
    })
    $("#webcam").on("hidden.bs.modal", function () {
        document.getElementById("camframe").src = "";
        //document.getElementById("cam_img").src = '';
    });
});
