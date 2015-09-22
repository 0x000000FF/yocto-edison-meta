DESCRIPTION = "assimp2json is a command line tool designed to expose the import capabilities of assimp, the Open Asset Import Library to WebGl developers. The tool takes a single 3d model as input file, imports it using assimp and converts the result to json."

LICENSE = "CLOSED"

SRC_URI = "git://github.com/assimp/assimp.git;protocol=https;branch=master"
 

SRCBRANCH = "${AUTOBRANCH}"
SRCREV = "${AUTOREV}"

S = "${WORKDIR}/git"

inherit cmake
EXTRA_OECMAKE = ""

FILES_${PN} += "/"

DEPENDS += "zlib"