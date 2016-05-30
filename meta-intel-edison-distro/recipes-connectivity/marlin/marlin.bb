DESCRIPTION = "marlin hex file for avr use"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

LICENSE = "CLOSED"

PV = "1.18"
PR = "r14"

RDEPENDS_${PN} = "systemd"
RDEPENDS_${PN} += "avr-isp"

SRC_URI = "file://Marlin.hex \
			file://marlin-install.service \
            file://marlin-install.sh \
            "

SYSTEMD_SERVICE_${PN} = "marlin-install.service"
SYSTEMD_AUTO_ENABLE = "enable"

S = "${WORKDIR}"

inherit systemd update-alternatives

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN} += "/etc/marlin-install.sh \
				/mostfun/Marlin.hex \
				"

do_install() {
	install -v -d  ${D}/mostfun/
    install -v -d  ${D}/etc/
    install -m 0755 marlin-install.sh ${D}/etc/
    install -m 0755 Marlin.hex ${D}/mostfun/

    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/marlin-install.service ${D}${systemd_unitdir}/system/
	fi
}