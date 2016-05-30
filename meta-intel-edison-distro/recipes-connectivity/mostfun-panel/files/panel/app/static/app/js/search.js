/**
 * Created by Administrator on 2015/7/28.
 */

(function ($, window, document) {

    $(document).ready(function () {
        $('#items').hide();
    });
    $("#search").click(function () {

        $.ajax({
            url: '/test',
            data: {'param': $('#param').val()},
            dataType: 'json',
            success: function () {
                var element1={modelURL:'http://statiwew',
                    modelName:'moxiangm',
                    authorURL:'statiwew',
                    authorName:'sfgf',
                    picURL:'http://statiwew',
                    buyURL:'http://statiwew',
                    viewURL:'http://statiwew',
                    star:78
                };
                var element2={modelURL:'http://statiwew',
                    modelName:'moxiangm',
                    authorURL:'statiwew',
                    authorName:'dshjdg',
                    picURL:'http://statiwew',
                    buyURL:'http://statiwew',
                    viewURL:'http://statiwew',
                    star:78
                };
                var element3={modelURL:'http://statiwew',
                    modelName:'moxiangm',
                    authorURL:'statiwew',
                    authorName:'suoer',
                    picURL:'http://statiwew',
                    buyURL:'http://statiwew',
                    viewURL:'http://statiwew',
                    star:78
                };
                var value =[element1,element2,element3];
                var l = {'list':value};
                var h = template('test',l);
                document.getElementById('content').innerHTML = h;
                $('#items').show();
            },
        });
    });
}(jQuery, window, document));