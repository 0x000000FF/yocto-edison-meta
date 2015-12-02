
DESCRIPTION = "mt7601 wifi chip driver"
SECTION = "kernel/userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = " \
		file://mt7601Uap.ko \
		file://rtnet7601Uap.ko \
		file://rtutil7601Uap.ko \
		file://RT2870AP.dat \
		"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /lib/modules/mt7601Uap.ko \
 /lib/modules/rtnet7601Uap.ko \
 /lib/modules/rtutil7601Uap.ko \
 /etc/Wireless/RT2870AP/RT2870AP.dat \
"

do_install() {
        install -v -d  ${D}/lib/modules
        install -v -d  ${D}/etc/Wireless/RT2870AP
		install -m 0755 mt7601Uap.ko ${D}/lib/modules/
		install -m 0755 rtnet7601Uap.ko ${D}/lib/modules/
		install -m 0755 rtutil7601Uap.ko ${D}/lib/modules/
		install -m 0755 RT2870AP.dat ${D}/etc/Wireless/RT2870AP/
}


