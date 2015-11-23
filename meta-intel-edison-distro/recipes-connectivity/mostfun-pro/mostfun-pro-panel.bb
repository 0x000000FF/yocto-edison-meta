DESCRIPTION = "Firmware files for use with Linux kernel"
SECTION = "kernel/userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://panel.des3"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r3"

S = "${WORKDIR}"

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/panel.des3\
"

do_install() {
        install -v -d  ${D}/mostfun/
        install -m 0755 panel.des3 ${D}/mostfun/
}
