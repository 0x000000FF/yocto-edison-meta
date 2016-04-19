DESCRIPTION = "mjpg streamer"
SECTION = "kernel/userland"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"


SRC_URI = "file://mjpg-streamer.tar.gz"

LICENSE = "CLOSED"

PV = "0.0"
PR = "r0"

S = "${WORKDIR}"

inherit allarch update-alternatives

FILESDIR = "${FILE_DIRNAME}/files/"

FILES_${PN}  += " \
 /
"

do_compile() {
    make
}

do_install() {
	install -v -d  ${D}/mostfun/mjpg-streamer
    move *  ${D}/mostfun/mjpg-streamer
}
