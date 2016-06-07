DESCRIPTION = "online update config file,the URLs"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

RDEPENDS_${PN} += "bash"

SRC_URI = "file://cnfeeds \
			file://usfeeds.conf \
            file://hkfeeds \
            file://eufeeds \
            file://myfeeds \
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
 /etc/opkg/cnfeeds \
 /etc/opkg/usfeeds.conf \
 /etc/opkg/hkfeeds \
 /etc/opkg/eufeeds \
 /etc/opkg/myfeeds \
 /etc/checkupdate.sh \
 /etc/checkpackages.sh \
"

do_install() {
	install -v -d  ${D}/etc/opkg/
    install -m 0755 cnfeeds ${D}/etc/opkg/
    install -m 0755 usfeeds.conf ${D}/etc/opkg/
    install -m 0755 hkfeeds ${D}/etc/opkg/
    install -m 0755 eufeeds ${D}/etc/opkg/
    install -m 0755 myfeeds ${D}/etc/opkg/
    install -m 0755 checkupdate.sh ${D}/etc/
    install -m 0755 checkpackages.sh ${D}/etc/
    if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
        install -d ${D}/${systemd_unitdir}/system
        install -m 644 ${WORKDIR}/checkupdate.service ${D}${systemd_unitdir}/system/
        install -m 644 ${WORKDIR}/checkpackages.service ${D}${systemd_unitdir}/system/
    fi
}
