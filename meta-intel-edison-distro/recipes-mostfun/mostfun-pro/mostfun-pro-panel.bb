DESCRIPTION = "lcd driver"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

RDEPENDS_${PN} = "mraa"
RDEPENDS_${PN} += "bash"

SRC_URI = "file://mostfun.des3 \
           file://panel-install.service \
           file://panel-install.sh \
           file://mostfun_panel.service"

LICENSE = "CLOSED"

PV = "1.22.fd85f9f"
PR = "r32"

SYSTEMD_SERVICE_${PN} = "panel-install.service"
SYSTEMD_SERVICE_${PN} += "mostfun_panel.service"
SYSTEMD_AUTO_ENABLE = "disable"

inherit systemd update-alternatives

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN} = "/etc/panel-install.sh \
        /mostfun/mostfun.des3 \
        "

do_install() {
    install -v -d  ${D}/mostfun/
    install -v -d  ${D}/etc/
    install -m 0755 panel-install.sh ${D}/etc/
    install -m 0755 mostfun.des3 ${D}/mostfun/

    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/panel-install.service ${D}${systemd_unitdir}/system/
        install -m 644 ${WORKDIR}/mostfun_panel.service ${D}${systemd_unitdir}/system/
    fi
}
