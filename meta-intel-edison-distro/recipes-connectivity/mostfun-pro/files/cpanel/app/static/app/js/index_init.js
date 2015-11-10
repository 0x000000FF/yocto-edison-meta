/**
 * Created by stao on 15-10-24.
 */
$(document).ready(function(){
    $.ajax({
            url: '/get_index',
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
                $.getScript('static/app/js/webcam.js');

                $.getScript('static/vendor/datatable/media/js/jquery.dataTables.min.js');
                $.getScript('static/vendor/datatable/extensions/datatable-bootstrap/js/dataTables.bootstrap.js');
                $.getScript('static/vendor/datatable/extensions/datatable-bootstrap/js/dataTables.bootstrapPagination.js');
                $.getScript('static/vendor/datatable/extensions/ColVis/js/dataTables.colVis.min.js');
                $.getScript('static/vendor/flot/jquery.flot.min.js');
                $.getScript('static/vendor/flot/jquery.flot.tooltip.min.js');
                $.getScript('static/vendor/flot/jquery.flot.resize.min.js');
                $.getScript('static/vendor/flot/jquery.flot.pie.min.js');
                $.getScript('static/vendor/flot/jquery.flot.time.min.js');
                $.getScript('static/vendor/flot/jquery.flot.categories.min.js');
                $.getScript('static/3dv/src/lib/detector.js');
                $.getScript('static/3dv/src/lib/three.min.js');
                $.getScript('static/3dv/src/Madeleine.js');
                $.getScript('static/app/js/International/Index.js');
                $.getScript('static/app/js/getfilelist.js',function(){
                    getfilelist();
                });
                $.getScript('static/app/js/gettemp.js',function(){
                    gettemp();
                });
                $.getScript('static/app/js/getstatus.js',function(){
                    getstatus();
                });
                $.getScript('static/app/js/math.js');
                $.getScript('static/app/js/index_ctrl.js');
                $.getScript('static/app/js/movectrl.js');
                $.getScript('static/app/js/phone-mode/index.js');
            }
        });
});