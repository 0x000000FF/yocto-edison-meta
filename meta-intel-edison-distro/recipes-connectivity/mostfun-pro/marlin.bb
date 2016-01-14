DESCRIPTION = "Firmware files for use with Linux kernel"
SECTION = "kernel/userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://Marlin.hex"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r1"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/avr_isp/Marlin.hex \
"

inherit allarch update-alternatives

do_install() {
		install -v -d  ${D}/mostfun/avr_isp/
        install -m 0755 Marlin.hex ${D}/mostfun/avr_isp/
}
