DESCRIPTION = "online update config file,the URLs"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://updateconfigdev.conf"

LICENSE = "CLOSED"

<<<<<<< HEAD:meta-intel-edison-distro/recipes-connectivity/updateconfigdev/updateconfigdev.bb
PV = "0.1"
=======
PV = "0.3"
>>>>>>> c80c8cc25ee4bd6944df95846766a99b39c3de9c:meta-intel-edison-distro/recipes-connectivity/mostfun-pro/updateconfig.bb
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
