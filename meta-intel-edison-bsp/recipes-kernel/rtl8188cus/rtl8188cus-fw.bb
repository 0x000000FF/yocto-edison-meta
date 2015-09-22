DESCRIPTION = "Firmware files for use with Linux kernel"
SECTION = "kernel"

FILESEXTRAPATHS_prepend := "${EDISONREPO_TOP_DIR}/meta-mostfun/wifi/rtlwifi/"

SRC_URI = "file://rtl8192cufw.bin"

LICENSE = "CLOSED"

PV = "1.0"
PR = "r0"

S = "${WORKDIR}"

inherit allarch update-alternatives

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /lib/firmware/rtlwifi/rtl8192cufw.bin \
"

do_install() {
        install -v -d  ${D}/lib/firmware/rtlwifi/
        install -m 0755 rtl8192cufw.bin ${D}/lib/firmware/rtlwifi/
}
