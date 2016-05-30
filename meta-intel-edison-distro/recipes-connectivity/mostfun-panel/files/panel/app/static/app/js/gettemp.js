// JavaScript source code
var data = [];
var e0temp_data = [];
var e0set_data = [];
var bedtemp_data = [];
var bedset_data = [];
var dataset;
var totalpoints = 100;
var updateinterval = 1000;
var bedtmp = '';
var e0tmp = '';
time_count = 0;
json_tempaf = [0, 0, 0, 0];
json_tempbf = [0, 0, 0, 0];
json_tempstep = [0, 0, 0, 0];
var now = new Date().getTime();
e0temp_name = "";
e0set_name = "";
bedtemp_name = "";
bedset_name = "";

$(document).ready(function () {
    bedtmp = $("#info_bedtemp").text();
    e0tmp = $("#info_e0temp").text();
});
function getdata() {
    if (--time_count <= 0) {
        time_count = 5;
        $.ajax({
            url: './get/alltemp',
            data: {},
            timeout: 3000,
            dataType: 'json',
            success: function (json) {
                for (i = 0; i < 2; i++) {
                    json_tempbf[i] = json_tempaf[i];
                    json_tempaf[i] = parseInt(json[i]);
                    if (((json_tempbf[i] == 0) && (json_tempaf[i] != 0)) || ((json_tempbf[i] != 0) && (json_tempaf[i] == 0)))
                        json_tempbf[i] = json_tempaf[i];
                    json_tempstep[i] = (json_tempaf[i] - json_tempbf[i]) / 5;
                }
                for (i = 2; i < 4; i++) {
                    json_tempbf[i] = parseInt(json[i]);
                    json_tempaf[i] = parseInt(json[i]);
                    json_tempstep[i] = parseInt(0);
                }
            },
            error: function () {
                if (lang == 'zh') {
                    msg = '请求超时，请检查网络';
                }
                else {
                    msg = 'Request timeout, please check';
                }
                $.notify({
                    message: msg,
                    status: 'warning'
                });
            }
        });
    }
    if (phone) {
        $('#e0temp').text(json_tempbf[0] + "°C");
        $('#bedtemp').text(json_tempbf[1] + "°C");
        $('#e0settemp').text(json_tempbf[2] + "°C");
        $('#bedsettemp').text(json_tempbf[3] + "°C");
        $("#info_e0temp").text(e0tmp + "：" + json_tempbf[0].toFixed(1) + "°C");
        $("#info_bedtemp").text(bedtmp + "：" + json_tempbf[1].toFixed(1) + "°C");
    } else {
        e0temp_data.shift();
        e0set_data.shift();
        bedtemp_data.shift();
        bedset_data.shift();
        var temp = [now += updateinterval, json_tempbf[0] += json_tempstep[0]];
        e0temp_data.push(temp);
        temp = [now, json_tempbf[1] += json_tempstep[1]];
        bedtemp_data.push(temp);

        temp = [now, json_tempbf[2] += json_tempstep[2]];
        e0set_data.push(temp);
        temp = [now, json_tempbf[3] += json_tempstep[3]];
        bedset_data.push(temp);
        $("#info_e0temp").text(e0tmp + "：" + json_tempbf[0].toFixed(1) + "°C");
        $("#info_bedtemp").text(bedtmp + "：" + json_tempbf[1].toFixed(1) + "°C");
        e0temp_name = "e0temp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp" + parseInt(json_tempbf[0]) + "°C";
        bedtemp_name = "bedtemp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp" + parseInt(json_tempbf[1]) + "°C";
        e0set_name = "e0settemp&nbsp&nbsp&nbsp" + parseInt(json_tempbf[2]) + "°C";
        bedset_name = "bedsettemp&nbsp" + parseInt(json_tempbf[3]) + "°C";
    }
}

var options = {
    series: {
        lines: {
            show: true,
            linewidth: 1.2,
            fill: true
        },
    },
    xaxis: {
        mode: "time",
        tickSize: [5, "second"],
        tickFormatter: function (v, axis) {
            var date = new Date(v);
            if (date.getSeconds() % 10 == 0) {
                var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
                var seconds = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
                return minutes + ":" + seconds;
            } else {
                return "";
            }
        },
        axisLabel: "Time",
        axisLabelUseCanvas: true,
        axisLabelFontSizePixels: 12,
        axisLabelFontFamily: 'Verdana, Arial',
        axisLabelPadding: 10
    },
    yaxis: {
        min: 0,
        max: 250,
        ticksize: 10,
        tickformatter: function (v, axis) {
            if (v % 10 == 0) {
                return v + "c";
            } else {
                return "";
            }
        },
        axislabel: "temp",
        axislabelusecanvas: true,
        axislabelfontsizepixels: 12,
        axislabelfontfamily: 'verdana, arial',
        axislabelpadding: 6
    },
    legend: {
        labelboxbordercolor: "#fff",
        position: "nw"
    },
    grid: {
        backgroundcolor: "#000000",
        tickcolor: "#008040"
    }
};
function update() {
    getdata();
    if (!phone) {
        dataset[1].label = e0temp_name;
        dataset[0].label = e0set_name;
        dataset[3].label = bedtemp_name;
        dataset[2].label = bedset_name;

        $.plot($("#flot-placeholder1"), dataset, options);
    }
    //setTimeout(update, updateinterval);
}

function gettemp() {
    while (e0temp_data.length < totalpoints) {
        var temp = [now += updateinterval, 0];
        e0temp_data.push(temp);
        e0set_data.push(temp);
        bedtemp_data.push(temp);
        bedset_data.push(temp);
    }
    getdata();

    if (!phone) {
        dataset = [
            {label: "e0settemp", data: e0set_data, color: "#00ff00"},
            {label: "e0temp", data: e0temp_data, color: "#006600"},
            {label: "bedsettemp", data: bedset_data, color: "#ffff00"},
            {label: "bedtemp", data: bedtemp_data, color: "#ff6600"},
        ];
        $.plot($("#flot-placeholder1"), dataset, options);
    }
    var timer_temp = setInterval("update()", updateinterval);
    //update();
}