DESCRIPTION = "lcd driver"
SECTION = "userland"

inherit systemd update-alternatives

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

RDEPENDS_${PN} = "mraa"

SRC_URI = "file://TFT_8340 \
           file://TFT_LCD.service \
           file://logo.bmp"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

SYSTEMD_SERVICE_${PN} = "TFT_LCD.service"
SYSTEMD_AUTO_ENABLE = "enable"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/TFT_8340 \
 /mostfun/logo.bmp"

do_install() {
    install -v -d  ${D}/mostfun/
    install -m 0755 TFT_8340 ${D}/mostfun/
    install -m 0755 logo.bmp ${D}/mostfun/

    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/TFT_LCD.service ${D}${systemd_unitdir}/system/
	fi
}
