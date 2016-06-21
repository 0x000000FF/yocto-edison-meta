DESCRIPTION = "avr-isp tool to flash avr chip"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://avr_isp.tar.gz"

LICENSE = "CLOSED"

PV = "0.1"
PR = "r1"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /mostfun/avr_isp/__init__.py \
 /mostfun/avr_isp/chipDB.py \
 /mostfun/avr_isp/intelHex.py \
 /mostfun/avr_isp/ispBase.py \
 /mostfun/avr_isp/stk.py \
"

do_install() {
		install -v -d  ${D}/mostfun/avr_isp/
        install -m 0755 __init__.py ${D}/mostfun/avr_isp/
        install -m 0755 chipDB.py ${D}/mostfun/avr_isp/
        install -m 0755 intelHex.py ${D}/mostfun/avr_isp/
        install -m 0755 ispBase.py ${D}/mostfun/avr_isp/
        install -m 0755 stk.py ${D}/mostfun/avr_isp/
}
