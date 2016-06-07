DESCRIPTION = "mt7601u Kernel Driver Sample"
HOMEPAGE = "https://github.com/notro/wireless.git"
SECTION = "kernel/modules"
PRIORITY = "optional"
LICENSE = "CLOSED"
RDEPENDS_fbtft = "kernel (${KERNEL_VERSION})"
DEPENDS = "virtual/kernel"
PR = "r0"

SRCREV = "${AUTOREV}"
SRC_URI = "git://github.com/0x000000FF/MT7601u.git;protocol=git"

S="${WORKDIR}/git/"

FILES_${PN}  += "/etc/Wireless/RT2870AP/RT2870AP.dat"

inherit module

do_compile() {
  unset CFLAGS CPPFLAGS CXXFLAGS LDFLAGS CC LD CPP
  oe_runmake 'MODPATH="${D}${base_libdir}/modules/${KERNEL_VERSION}/kernel/drivers/net/wireless" ' \
             'KDIR="${STAGING_KERNEL_DIR}"' \
             'KERNEL_VERSION="${KERNEL_VERSION}"' \
             'CC="${KERNEL_CC}"' \
             'LD="${KERNEL_LD}"'
}

do_install() {
   install -d ${D}${base_libdir}/modules/${KERNEL_VERSION}/kernel/drivers/net/wireless
   install -v -d  ${D}/etc/Wireless/RT2870AP

   install -m 0644 ${S}/src/os/linux/*${KERNEL_OBJECT_SUFFIX} ${D}${base_libdir}/modules/${KERNEL_VERSION}/kernel/drivers/net/wireless
   install -m 0755 ${S}/etc/Wireless/RT2870AP/RT2870AP.dat ${D}/etc/Wireless/RT2870AP/
}

SRC_URI[md5sum] = "082723afbbe117b29c271813a525b74f"
SRC_URI[sha256sum] = "342a1e12f39b038962b5ea0371df6b94604c9385130a07db4686ebc8ea478624"
