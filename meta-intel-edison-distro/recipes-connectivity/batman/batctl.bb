DESCRIPTION = "Control application for B.A.T.M.A.N. routing protocol kernel module for multi-hop ad-hoc mesh networks."
HOMEPAGE = "http://www.open-mesh.net/"
SECTION = "console/network"
PRIORITY = "optional"

LICENSE = "CLOSED"

RDEPENDS_${PN} = "kernel-module-batman-adv"
DEPENDS = "libnl"

SRC_URI = "file://batctl-2015.2.tar.gz"
#     file://patch.patch"
SRC_URI[md5sum] = "3db00af0b3cf55136babe06aa666e15f"
#SRC_URI[sha256sum] = "77509ed70232ebc0b73e2fa9471ae13b12d6547d167dda0a82f7a7fad7252c36"

EXTRA_OEMAKE = 'STAGING_INC="${STAGING_INC}"'

do_compile() {
  oe_runmake
}

do_install() {
  install -d ${D}${bindir}
  install -m 0755 batctl ${D}${bindir}
}