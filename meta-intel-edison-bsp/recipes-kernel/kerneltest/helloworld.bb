SUMMARY = "Example of how to build an external Linux kernel module"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=d41d8cd98f00b204e9800998ecf8427e"


FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

inherit module

PR = "r0"
PV = "0.1"

SRC_URI = "file://helloworld.c"
SRC_URI += "file://Makefile"

S = "${WORKDIR}"

# The inherit of module.bbclass will automatically name module packages with
# "kernel-module-" prefix as required by the oe-core build environment.

