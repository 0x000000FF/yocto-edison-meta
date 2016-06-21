DESCRIPTION = "auto mount and umount SDcard and USB storage"
SECTION = "userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

RDEPENDS_${PN} += "bash"

SRC_URI = "file://100-usbstorage.rules \
			file://autoinstall.sh \
			file://automount.sh \
			file://autoumount.sh"

LICENSE = "CLOSED"

PV = "0.3"
PR = "r1"

S = "${WORKDIR}"

inherit allarch update-alternatives

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /lib/udev/rules.d/100-usbstorage.rules \
 /etc/automount.sh \
 /etc/autoumount.sh \
 /etc/autoinstall.sh \
"

do_install() {
	install -v -d  ${D}/etc/
	install -v -d  ${D}/lib/udev/rules.d/
    install -m 0755 automount.sh ${D}/etc/
    install -m 0755 autoumount.sh ${D}/etc/
    install -m 0755 autoinstall.sh ${D}/etc/
    install -m 0755 100-usbstorage.rules ${D}/lib/udev/rules.d/
}

