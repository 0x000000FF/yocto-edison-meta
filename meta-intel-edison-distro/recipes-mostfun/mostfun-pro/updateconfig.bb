DESCRIPTION = "online update config file,the URLs"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://myfeeds.conf"

LICENSE = "CLOSED"

PV = "0.3"
PR = "r1"

S = "${WORKDIR}"

inherit allarch update-alternatives

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /etc/opkg/myfeeds.conf\
"

do_install() {
	install -v -d  ${D}/etc/opkg/
    install -m 0755 myfeeds.conf ${D}/etc/opkg/
}
