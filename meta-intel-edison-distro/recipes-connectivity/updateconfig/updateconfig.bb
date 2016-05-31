DESCRIPTION = "online update config file,the URLs"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

RDEPENDS_${PN} += "bash"

SRC_URI = "file://cn_feeds.conf \
			file://us_feeds.conf \
            file://hk_feeds.conf \
            file://eu_feeds.conf \
            file://my_feeds.conf \
			file://checkupdate.sh \
			file://checkpackages.sh \
			file://checkupdate.service \
			file://checkpackages.service \
			"

LICENSE = "CLOSED"

PV = "0.6"
PR = "r4"

SYSTEMD_SERVICE_${PN} = "checkupdate.service"
SYSTEMD_SERVICE_${PN} += "checkpackages.service"
SYSTEMD_AUTO_ENABLE = "disable"

S = "${WORKDIR}"

inherit systemd update-alternatives

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /etc/opkg/cn_feeds.conf \
 /etc/opkg/us_feeds.conf \
 /etc/opkg/hk_feeds.conf \
 /etc/opkg/eu_feeds.conf \
 /etc/opkg/my_feeds.conf \
 /etc/checkupdate.sh \
 /etc/checkpackages.sh \
"

do_install() {
	install -v -d  ${D}/etc/opkg/
    install -m 0755 cn_feeds.conf ${D}/etc/opkg/
    install -m 0755 us_feeds.conf ${D}/etc/opkg/
    install -m 0755 hk_feeds.conf ${D}/etc/opkg/
    install -m 0755 eu_feeds.conf ${D}/etc/opkg/
    install -m 0755 my_feeds.conf ${D}/etc/opkg/
    install -m 0755 checkupdate.sh ${D}/etc/
    install -m 0755 checkpackages.sh ${D}/etc/
    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/checkupdate.service ${D}${systemd_unitdir}/system/
        install -m 644 ${WORKDIR}/checkpackages.service ${D}${systemd_unitdir}/system/
    fi
}
