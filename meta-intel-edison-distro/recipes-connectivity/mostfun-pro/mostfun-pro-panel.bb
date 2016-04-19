DESCRIPTION = "mostfun pro 3D printer controller"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

inherit allarch update-alternatives

DEPENDS = "decode"

SRC_URI = "file://mostfun.des3"

LICENSE = "CLOSED"

PV = "1.5.4437c4e"
PR = "r16"

S = "${WORKDIR}"

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/mostfun.des3\
"

do_install() {
        install -v -d  ${D}/mostfun/
        install -m 0755 mostfun.des3 ${D}/mostfun/
}
