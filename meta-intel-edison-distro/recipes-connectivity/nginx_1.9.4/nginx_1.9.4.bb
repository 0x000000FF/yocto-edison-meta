DESCRIPTION = "nginx [engine x] is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP proxy server, originally written by Igor Sysoev."
HOMEPAGE = "https://http://nginx.org/"
SECTION = "devel/nginx"
LICENSE = "CLOSED"

PR = "r0"

SRC_URI = "http://nginx.org/download/nginx-${PV}.tar.gz"

SRC_URI[md5sum] = "27322fbb4b265c0e0cc548f5e6b7f201"
SRC_URI[sha256sum] = "479b0c03747ee6b2d4a21046f89b06d178a2881ea80cfef160451325788f2ba8"



S = "${WORKDIR}/nginx-${PV}"

inherit allarch update-alternatives


FILES_${PN}  += "\"


do_compile() {
	./configure
    make
#    make install
}

do_install() {

}

RDEPENDS_${PN} += "pcre,zlib"