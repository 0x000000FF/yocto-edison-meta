/**
 * Created by stao on 15-10-16.
 */
$(function(){
	$("#help_md>li>a>span").click(function(){
		sid = $(this).attr('id');
		$.ajax({
            url: '/get-help',
            data:{
                'file_name': sid
            },
            type: 'POST',
            dataType: 'json',
            success:function(data){
                var converter = new Markdown.Converter();
                var shtml = converter.makeHtml(data);
                $('#fadeOut').trigger('click');
                setTimeout(function(){
                    $('#panel-anim-fadeOut').html(shtml);
                },860);
            }
        });
    });
});
