DESCRIPTION = "mostfun models"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://extruder_air-duct.gcode \
			file://extruder_air-duct.stl \
			file://extruder_cleaner.gcode \
			file://extruder_cleaner.stl \
			file://extruder_gearing.gcode \
			file://extruder_gearing.stl \
			file://extruder_guider.gcode \
			file://extruder_guider.stl \
			"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /home/mostfuncp/gcode/extruder_air-duct.gcode \
 /home/mostfuncp/model/extruder_air-duct.stl \
 /home/mostfuncp/gcode/extruder_cleaner.gcode \
 /home/mostfuncp/model/extruder_cleaner.stl \
 /home/mostfuncp/gcode/extruder_gearing.gcode \
 /home/mostfuncp/model/extruder_gearing.stl \
 /home/mostfuncp/gcode/extruder_guider.gcode \
 /home/mostfuncp/model/extruder_guider.stl \
"
inherit allarch update-alternatives
do_install() {
        install -v -d  ${D}/home/mostfuncp/gcode
        install -v -d  ${D}/home/mostfuncp/model
        install -m 0755 extruder_air-duct.gcode ${D}/home/mostfuncp/gcode
        install -m 0755 extruder_cleaner.gcode ${D}/home/mostfuncp/gcode
        install -m 0755 extruder_gearing.gcode ${D}/home/mostfuncp/gcode
        install -m 0755 extruder_guider.gcode ${D}/home/mostfuncp/gcode
        install -m 0755 extruder_air-duct.stl ${D}/home/mostfuncp/model
        install -m 0755 extruder_cleaner.stl ${D}/home/mostfuncp/model
        install -m 0755 extruder_gearing.stl ${D}/home/mostfuncp/model
        install -m 0755 extruder_guider.stl ${D}/home/mostfuncp/model
}
