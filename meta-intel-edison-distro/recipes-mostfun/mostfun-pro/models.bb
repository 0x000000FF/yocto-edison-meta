DESCRIPTION = "mostfun pro 3D printer test models"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://birdcage.stl \
           file://birdcage.gcode"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += "/home/birdcage.stl \
           /home/birdcage.gcode"

inherit allarch update-alternatives

do_install() {
        install -v -d  ${D}/home/gcode
        install -v -d  ${D}/home/model
        install -m 0755 birdcage.gcode ${D}/home/gcode
        install -m 0755 birdcage.stl ${D}/home/model
}
