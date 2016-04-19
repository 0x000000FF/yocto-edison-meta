DESCRIPTION = "panel service file"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

inherit systemd update-alternatives 

SRC_URI = "file://mostfun_panel.service"

LICENSE = "CLOSED"

PV = "0.1"
PR = "r0"

SYSTEMD_SERVICE_${PN} = "mostfun_panel.service"
SYSTEMD_AUTO_ENABLE = "enable"

S = "${WORKDIR}"

inherit allarch update-alternatives

FILESDIR = "${FILE_DIRNAME}/files/"

do_install() {
    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/mostfun_panel.service ${D}${systemd_unitdir}/system/
	fi
}

