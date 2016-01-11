DESCRIPTION = "for mostfin pro camera"

DEPENDS += "jpeg"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://mjpg_streamer \
			file://input_uvc.so \
			file://output_file.so \
			"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

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
}
