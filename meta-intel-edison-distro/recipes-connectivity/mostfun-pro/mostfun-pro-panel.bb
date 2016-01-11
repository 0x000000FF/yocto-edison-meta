DESCRIPTION = "mostfun pro 3D printer controller"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://mostfun.des3"

LICENSE = "CLOSED"

PV = "1.1"
PR = "r8"

S = "${WORKDIR}"

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/mostfun.des3\
"
inherit allarch update-alternatives

do_install() {
        install -v -d  ${D}/mostfun/
        install -m 0755 mostfun.des3 ${D}/mostfun/
}
