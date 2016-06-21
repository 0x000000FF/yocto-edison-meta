DESCRIPTION = "init file"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

inherit systemd update-alternatives 

SRC_URI = "file://mountupdate.sh \
           file://mountupdate.service"

LICENSE = "CLOSED"

PV = "0.1"
PR = "r0"

SYSTEMD_SERVICE_${PN} = "mountupdate.service"
SYSTEMD_AUTO_ENABLE = "disable"

S = "${WORKDIR}"

inherit allarch update-alternatives

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /etc/init.d/mountupdate.sh\
"

do_install() {
	install -v -d  ${D}/etc/
    install -m 0755 mountupdate.sh ${D}/etc/

    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/mountupdate.service ${D}${systemd_unitdir}/system/
	fi
}

