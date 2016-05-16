DESCRIPTION = "model slicer"

LIC_FILES_CHKSUM = "file://LICENSE;md5=d41d8cd98f00b204e9800998ecf8427e"
FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://CuraEngine.mostfun \
			file://default.cfg"

LICENSE = "AGPLv3"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/slicer\
"

do_install() {
        install -v -d  ${D}/mostfun/slicer/
        install -m 0755 CuraEngine.mostfun ${D}/mostfun/slicer/
        install -m 0755 default.cfg ${D}/mostfun/slicer/
}
