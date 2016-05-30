/**
 * Created by stao on 15-10-24.
 */
function movemid() {
            $.get('./send/G1 F4000 X0 Y0', function (data) {
                if (lang = "zh") {
                    msg = "喷头归位";
                }
                else {
                    msg = "Extruder homing";
                }
                $.notify({
                    message: msg,
                    status: 'info'
                });
                $.get('./send/G1 F4000 X60 Y80', function (data) {
                    if (lang = "zh") {
                        msg = "喷头居中";
                    }
                    else {
                        msg = "Extruder center";
                    }
                    $.notify({
                        message: msg,
                        status: 'info'
                    });
                });
            });
        }