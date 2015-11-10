DESCRIPTION = "lcd driver"
SECTION = "kernel/userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://TFT_8340"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/TFT_8340\
"

do_install() {
        install -v -d  ${D}/mostfun/
        install -m 0755 TFT_8340 ${D}/mostfun/
}
