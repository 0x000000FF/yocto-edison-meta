DESCRIPTION = "for mostfun pro camera"

DEPENDS += "jpeg"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

inherit systemd update-alternatives

SRC_URI = "file://mjpg_streamer \
			file://mjpg_streamer.service \
			file://input_uvc.so \
			file://output_file.so \
			"

LICENSE = "CLOSED"

PV = "0.1"
PR = "r1"

SYSTEMD_SERVICE_${PN} = "mjpg_streamer.service"
SYSTEMD_AUTO_ENABLE = "enable"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/mjpgstreamer/mjpg_streamer \
 /mostfun/mjpgstreamer/input_uvc.so \
 /mostfun/mjpgstreamer/output_file.so \
"

do_install() {
        install -v -d  ${D}/mostfun/mjpgstreamer/
        install -m 0755 mjpg_streamer ${D}/mostfun/mjpgstreamer/
        install -m 0755 input_uvc.so ${D}/mostfun/mjpgstreamer/
        install -m 0755 output_file.so ${D}/mostfun/mjpgstreamer/

    	if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        	install -d ${D}/${systemd_unitdir}/system
        	install -m 644 ${WORKDIR}/mjpg_streamer.service ${D}${systemd_unitdir}/system/
		fi
}
