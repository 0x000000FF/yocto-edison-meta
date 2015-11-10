DESCRIPTION = "used by nginx"
HOMEPAGE = ""
SECTION = "devel/nginx"
LICENSE = "CLOSED"

PR = "r0"

SRC_URI = "ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${PV}.tar.gz"

SRC_URI[md5sum] = "6e0cc6d1bdac7a4308151f9b3571b86e"
SRC_URI[sha256sum] = "19d490a714274a8c4c9d131f651489b8647cdb40a159e9fb7ce17ba99ef992ab"


S = "${WORKDIR}/pcre-${PV}"

inherit allarch update-alternatives

FILES_${PN}  += "\"

do_configure() {
	./configure
}

do_compile() {
	
	make 
	make install
}

do_install() {

}