DESCRIPTION = "for mostfun pro usbhub"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

inherit systemd update-alternatives

SRC_URI = "file://usbhub.service \
            file://start_usbhub.sh"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

SYSTEMD_SERVICE_${PN} = "usbhub.service"
SYSTEMD_AUTO_ENABLE = "enable"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /etc/init.d/start_usbhub.sh\
"

do_install() {
    install -v -d  ${D}/etc/
    install -m 0755 start_usbhub.sh ${D}/etc/

	if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
    	install -d ${D}/${systemd_unitdir}/system
    	install -m 644 ${WORKDIR}/usbhub.service ${D}${systemd_unitdir}/system/
	fi
}
