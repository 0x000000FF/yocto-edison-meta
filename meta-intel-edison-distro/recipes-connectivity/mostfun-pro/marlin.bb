DESCRIPTION = "Firmware files for use with Linux kernel"
SECTION = "kernel/userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://Marlin.hex"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/Marlin.hex \
"

do_install() {
		install -v -d  ${D}/mostfun/avr_isp/
        install -m 0755 Marlin.hex ${D}/mostfun/
}
