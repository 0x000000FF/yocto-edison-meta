DESCRIPTION = "fbtft  Kernel Driver Sample"
HOMEPAGE = "https://github.com/notro/fbtft.git"
SECTION = "kernel/modules"
PRIORITY = "optional"
LICENSE = "CLOSED"
RDEPENDS_fbtft = "kernel (${KERNEL_VERSION})"
DEPENDS = "virtual/kernel"
PR = "r0"

SRCREV = "71994224c5ed951eab7ca9da2c919456d1632d15"
SRC_URI = "git://github.com/notro/fbtft.git;protocol=git \
	   file://dma_disable.patch \
	   file://cansleep.patch"

S="${WORKDIR}/git/"

inherit module

do_compile() {
  unset CFLAGS CPPFLAGS CXXFLAGS LDFLAGS CC LD CPP
  oe_runmake 'MODPATH="${D}${base_libdir}/modules/${KERNEL_VERSION}/kernel/drivers/video/fbtft" ' \
             'KDIR="${STAGING_KERNEL_DIR}"' \
             'KERNEL_VERSION="${KERNEL_VERSION}"' \
             'CC="${KERNEL_CC}"' \
             'LD="${KERNEL_LD}"'
}

do_install() {
   install -d ${D}${base_libdir}/modules/${KERNEL_VERSION}/kernel/drivers/video/fbtft

   install -m 0644 ${S}/f*${KERNEL_OBJECT_SUFFIX} ${D}${base_libdir}/modules/${KERNEL_VERSION}/kernel/drivers/video/fbtft
}

SRC_URI[md5sum] = "082723afbbe117b29c271813a525b74f"
SRC_URI[sha256sum] = "342a1e12f39b038962b5ea0371df6b94604c9385130a07db4686ebc8ea478624"
