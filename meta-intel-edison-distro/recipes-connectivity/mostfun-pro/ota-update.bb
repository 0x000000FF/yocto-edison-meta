DESCRIPTION = "Firmware files for use with Linux kernel"
SECTION = "kernel/userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://toFlash.mostfun"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

inherit allarch update-alternatives

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /ota-file/toFlash.mostfun\
"

do_install() {
        install -v -d  ${D}/ota-file/
#        losetup -o 8192 /dev/loop0 /dev/disk/by-partlabel/update
#        mount /dev/loop0 /update
        cp toFlash.mostfun ${D}/ota-file/
}
