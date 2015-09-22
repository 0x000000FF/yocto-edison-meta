DESCRIPTION = "Blinks the Edison LED"
SECTION = "base"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://blink-led"
SRC_URI += "file://blink-led.service"

S = "${WORKDIR}"

do_install() {
        install -d ${D}${bindir}
        install -m 0755 blink-led ${D}${bindir}

        # Copy service file
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/blink-led.service ${D}/${systemd_unitdir}/system
}

FILES_${PN} += "${base_libdir}/systemd/system/blink-led.service"
FILES_${PN} += "${bindir}/blink-led"
