DESCRIPTION = "online update config file,the URLs"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://updateconfigdev.conf"

LICENSE = "CLOSED"

PV = "0.1"
PR = "r1"

S = "${WORKDIR}"

inherit allarch update-alternatives

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /etc/opkg/updateconfigdev.conf\
"

do_install() {
	install -v -d  ${D}/etc/opkg/
    install -m 0755 updateconfigdev.conf ${D}/etc/opkg/
}
