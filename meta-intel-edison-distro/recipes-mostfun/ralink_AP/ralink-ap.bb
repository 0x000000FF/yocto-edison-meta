SECTION = "kernel/userland"
LICENSE = "CLOSED"

inherit systemd

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

PV = "1.0"
PR = "r2"

SYSTEMD_SERVICE_${PN} = "udhcpd-for-ra0.service"
SYSTEMD_AUTO_ENABLE = "disable"
SRC_URI = " \
    file://udhcpd-for-ra0.service \
    file://udhcpd-for-ra0.conf \
    file://loadra0.sh \
    file://unloadra0.sh \
"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"


do_install() {
    install -d ${D}/etc/Wireless/RT2870AP
    install -m 755 ${WORKDIR}/udhcpd-for-ra0.conf ${D}/etc/Wireless/RT2870AP/
    install -m 755 ${WORKDIR}/loadra0.sh ${D}/etc/
    install -m 755 ${WORKDIR}/unloadra0.sh ${D}/etc/

    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/udhcpd-for-ra0.service ${D}${systemd_unitdir}/system/
        
    fi
}

