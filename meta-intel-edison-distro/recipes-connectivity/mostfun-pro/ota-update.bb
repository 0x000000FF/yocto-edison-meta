DESCRIPTION = "files for update sys"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

RDEPENDS_${PN} = "mraa"
RDEPENDS_${PN} += "bash"

SRC_URI = "file://update.sh \
           file://update.service"

LICENSE = "CLOSED"

PV = "0.1"
PR = "r1"

SYSTEMD_SERVICE_${PN} = "update.service"
SYSTEMD_AUTO_ENABLE = "disable"

inherit systemd update-alternatives

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /etc/update.sh"

do_install() {
    install -v -d  ${D}/etc/
    install -m 0755 update.sh ${D}/etc/

    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/update.service ${D}${systemd_unitdir}/system/
	fi
}
