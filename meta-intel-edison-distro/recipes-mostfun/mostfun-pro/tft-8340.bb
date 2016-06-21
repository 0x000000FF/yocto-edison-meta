DESCRIPTION = "lcd driver"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

RDEPENDS_${PN} = "mraa"
RDEPENDS_${PN} += "bash"

SRC_URI = "file://TFT_8340 \
           file://TFT_LCD.service \
           file://creatpidfile.sh \
           file://freshpage.sh \
           file://logo.bmp \
           file://upgrading.bmp"

LICENSE = "CLOSED"

PV = "0.6"
PR = "r4"

SYSTEMD_SERVICE_${PN} = "TFT_LCD.service"
SYSTEMD_AUTO_ENABLE = "enable"

inherit systemd update-alternatives

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /etc/creatpidfile.sh \
 /etc/freshpage.sh \
 /mostfun/TFT/TFT_8340 \
 /mostfun/TFT/logo.bmp \
 /mostfun/TFT/upgrading.bmp"

do_install() {
    install -v -d  ${D}/mostfun/TFT/
    install -v -d  ${D}/etc/
    install -m 0755 creatpidfile.sh ${D}/etc/
    install -m 0755 freshpage.sh ${D}/etc/
    install -m 0755 TFT_8340 ${D}/mostfun/TFT/
    install -m 0755 upgrading.bmp ${D}/mostfun/TFT/
    install -m 0755 logo.bmp ${D}/mostfun/TFT/

    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/TFT_LCD.service ${D}${systemd_unitdir}/system/
	fi
}
