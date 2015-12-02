SECTION = "kernel/userland"
LICENSE = "CLOSED"

inherit systemd

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SYSTEMD_SERVICE_${PN} = "udhcpd-for-ra0.service"
SYSTEMD_AUTO_ENABLE = "disable"
SRC_URI = " \
    file://udhcpd-for-ra0.service \
    file://udhcpd-for-ra0.conf \
"

S = "${WORKDIR}"

FILESDIR = "${FILE_DIRNAME}/files/"

do_install() {
    install -d ${D}/etc/Wireless/RT2870AP
    install -m 755 ${WORKDIR}/udhcpd-for-ra0.conf ${D}/etc/Wireless/RT2870AP/
    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
            # Install hostapd service
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/udhcpd-for-ra0.service ${D}${systemd_unitdir}/system/
        
    fi
}

