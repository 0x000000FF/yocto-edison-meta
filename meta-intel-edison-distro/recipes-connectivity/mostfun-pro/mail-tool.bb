DESCRIPTION = "mostfun pro 3D printer controller"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://mail-tool.tar.gz"

LICENSE = "CLOSED"

PV = "0.1"
PR = "r1"

S = "${WORKDIR}"

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/mail-tool/main.py \
 /mostfun/mail-tool/mail-config.ini \
"
inherit allarch update-alternatives

do_install() {
        install -v -d  ${D}/mostfun/mail-tool
        install -m 0755 main.py ${D}/mostfun/mail-tool/
        install -m 0755 mail-config.ini ${D}/mostfun/mail-tool/
}
