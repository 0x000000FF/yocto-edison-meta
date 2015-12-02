DESCRIPTION = "Firmware files for use with Linux kernel"
SECTION = "kernel/userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://mostfun.des3"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

inherit allarch

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/mostfun.des3\
"

do_install() {
        install -v -d  ${D}/mostfun/
        install -m 0755 mostfun.des3 ${D}/mostfun/
}
