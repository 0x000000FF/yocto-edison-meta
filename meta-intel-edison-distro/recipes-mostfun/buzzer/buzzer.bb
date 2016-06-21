DESCRIPTION = "mostfun buzzer"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://buzzer"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/buzzer\
"

do_install() {
        install -v -d  ${D}/mostfun/
        install -m 0755 buzzer ${D}/mostfun/
}
