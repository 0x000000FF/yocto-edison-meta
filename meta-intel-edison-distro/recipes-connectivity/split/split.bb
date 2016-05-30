DESCRIPTION = "lcd driver"

LIC_FILES_CHKSUM = "file://LICENSE;md5=73f1eb20517c55bf9493b7dd6e480788"
FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://CuraEngine.most"

LICENSE = "AGPLv3"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/CuraEngine.most\
"

do_install() {
        install -v -d  ${D}/mostfun/
        install -m 0755 CuraEngine.most ${D}/mostfun/
}
