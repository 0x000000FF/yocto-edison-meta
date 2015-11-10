/**
 * Created by stao on 15-10-16.
 */



$(function(){
	$("#help_md>li>a>span").click(function(){
		sid = $(this).attr('id');
		alert(sid);
		$.ajax({
            url: '/get-help',
            data:{
                'file_name': sid
            },
            type: 'POST',
            dataType: 'json',
            success:function(data){
                alert("dfdfdf");
                var converter = new Markdown.Converter();
                var shtml = converter.makeHtml(data);
                $('.main-content').html(shtml);
            }
        });
    });
});
