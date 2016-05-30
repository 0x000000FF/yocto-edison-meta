/**
 * Created by stao on 15-10-24.
 */
$(function(){
	$("#title_getmodel").click(function(){
		$.ajax({
            url: '/get_most3d',
            type: 'POST',
            dataType: 'html',
            success:function(data){
                $('#fadeOut').trigger('click');
                setTimeout(function(){
                $.getScript('static/vendor/chosen/chosen.jquery.min.js');
                $.getScript('static/vendor/slimscroll/jquery.slimscroll.min.js');
                $.getScript('static/app/js/phone-check.js');
                $.getScript('static/app/js/app.js');
                $.getScript('static/app/js/International/jquery.i18n.properties-1.0.9.js');
                $.getScript('static/app/js/International/langSet.js');
                $.getScript('static/app/js/International/base.js');
                $.getScript('static/app/js/webcam.js');
                $.getScript('static/3dv/src/lib/detector.js');

                $.getScript('static/app/js/International/Most3D.js');
                $.getScript('static/app/js/TempleEngine/template-debug.js');
                $.getScript('static/app/js/search.js');
                $('#panel-anim-fadeOut').html(data);
            },860);
            }
        });
    });
});