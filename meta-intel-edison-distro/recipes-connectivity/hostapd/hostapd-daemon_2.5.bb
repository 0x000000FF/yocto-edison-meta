HOMEPAGE = "http://hostap.epitest.fi"
SECTION = "kernel/userland"
LICENSE = "GPLv2 | BSD"
LIC_FILES_CHKSUM = "file://README;md5=4d53178f44d4b38418a4fa8de365e11c"
DEPENDS = "libnl openssl"
SUMMARY = "User space daemon for extended IEEE 802.11 management"

inherit systemd

SYSTEMD_SERVICE_${PN} = "hostapd.service udhcpd-for-hostapd.service"
SYSTEMD_AUTO_ENABLE = "disable"

SRC_URI = " \
    file://hostapd-2.5.tar.gz \
    file://defconfig \
    file://hostapd.service \
    file://udhcpd-for-hostapd.service \
    file://hostapd.conf-sane \
    file://udhcpd-for-hostapd.conf \
"

S = "${WORKDIR}/hostapd-${PV}/hostapd"

do_configure() {
    install -m 0644 ${WORKDIR}/defconfig ${S}/.config
    echo "CFLAGS +=\"-I${STAGING_INCDIR}/libnl3\"" >> ${S}/.config
}

do_compile() {
    make
}

do_install() {
    install -d ${D}${sbindir}
    install -m 0755 ${S}/hostapd ${D}${sbindir}
    install -m 0755 ${S}/hostapd_cli ${D}${sbindir}

    install -d ${D}${sysconfdir}/hostapd
    install -m 0644 ${WORKDIR}/hostapd.conf-sane ${D}${sysconfdir}/hostapd/hostapd.conf
    install -m 0644 ${WORKDIR}/udhcpd-for-hostapd.conf ${D}${sysconfdir}/hostapd

    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        # Install hostapd service
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/hostapd.service ${D}${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/udhcpd-for-hostapd.service ${D}${systemd_unitdir}/system
    fi
}

SRC_URI[md5sum] = "69f9cec3f76d74f402864a43e4f8624f"
SRC_URI[sha256sum] = "8e272d954dc0d7026c264b79b15389ec2b2c555b32970de39f506b9f463ec74a"
