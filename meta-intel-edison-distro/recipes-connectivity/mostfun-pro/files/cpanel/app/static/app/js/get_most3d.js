/**
 * Created by stao on 15-10-24.
 */
$(function(){
	$("#most3d").click(function(){
		$.ajax({
            url: '/get_most3d',
            type: 'POST',
            dataType: 'html',
            success:function(data){
                $('.main-content').html(data);
                $.getScript('static/vendor/jquery/jquery.min.js');
                $.getScript('static/vendor/bootstrap/js/bootstrap.min.js');
                $.getScript('static/vendor/chosen/chosen.jquery.min.js');
                $.getScript('static/vendor/slider/js/bootstrap-slider.js');
                $.getScript('static/vendor/filestyle/bootstrap-filestyle.min.js');
                $.getScript('static/vendor/animo/animo.min.js');
                $.getScript('static/vendor/sparklines/jquery.sparkline.min.js');
                $.getScript('static/vendor/slimscroll/jquery.slimscroll.min.js');
                $.getScript('static/app/js/phone-check.js');
                $.getScript('static/app/js/app.js');
                $.getScript('static/app/js/International/jquery.i18n.properties-1.0.9.js');
                $.getScript('static/app/js/International/langSet.js');
                $.getScript('static/app/js/International/base.js');
                $.getScript('static/app/js/webcam.js');
                $.getScript('static/3dv/src/lib/detector.js');
                $.getScript('static/3dv/src/lib/detector.js');
                $.getScript('static/3dv/src/lib/detector.js');

                $.getScript('static/app/js/International/Most3D.js');
                $.getScript('static/app/js/TempleEngine/template-debug.js');
                $.getScript('static/app/js/search.js');
            }
        });
    });
});