DESCRIPTION = "init file"
SECTION = "kernel/userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://start.sh"

LICENSE = "CLOSED"

PV = "0.1"
PR = "r0"

S = "${WORKDIR}"

inherit allarch update-alternatives

#FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /etc/init.d/start.sh\
"

do_install() {
	install -v -d  ${D}/etc/init.d/
#	install -v -d  ${D}/update
    install -m 0755 start.sh ${D}/etc/init.d/
}
