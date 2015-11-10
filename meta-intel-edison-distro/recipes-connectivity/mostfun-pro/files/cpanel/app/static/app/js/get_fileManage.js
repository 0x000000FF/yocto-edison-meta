/**
 * Created by stao on 15-10-24.
 */
$(function(){
	$("#tlt_mag").click(function(){
		$.ajax({
            url: '/get_fileManage',
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

                $.getScript('static/vendor/datatable/media/js/jquery.dataTables.min.js');
                $.getScript('static/vendor/datatable/extensions/datatable-bootstrap/js/dataTables.bootstrap.js');
                $.getScript('static/vendor/datatable/extensions/datatable-bootstrap/js/dataTables.bootstrapPagination.js');
                $.getScript('static/vendor/datatable/extensions/ColVis/js/dataTables.colVis.min.js');
                $.getScript('static/3dv/src/lib/detector.js');
                $.getScript('static/3dv/src/lib/three.min.js');
                $.getScript('static/3dv/src/Madeleine.js');
                $.getScript('static/app/js/International/filemanage.js');
                $.getScript('static/app/js/getfilelistmin.js',function(){
                    getfilelistmin();
                });
                $.getScript('static/app/js/piechartmath.js');
                $.getScript('static/app/js/phone-mode/fileManage.j');
            }
        });
    });
});