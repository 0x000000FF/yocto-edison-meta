DESCRIPTION = "Firmware files for use with Linux kernel"
SECTION = "kernel/userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://decode.mostfun"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

inherit allarch update-alternatives

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/decode.mostfun\
"

do_install() {
	install -v -d  ${D}/mostfun/
    install -m 0755 decode.mostfun ${D}/mostfun/
}
