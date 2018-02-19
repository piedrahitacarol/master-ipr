# Authors: see AUTHORS.md at project root.
# CopyPolicy: released under the terms of the LGPLv2.1, see LICENSE at project root.
# URL: https://github.com/jgvictores/2018-ptmr

find_package(YARP REQUIRED)
list(APPEND CMAKE_MODULE_PATH ${YARP_MODULE_PATH})
include(YarpInstallationHelpers)
#yarp_configure_external_installation(2018-ptmr)  # Commenting out because not using generated vars

yarp_install(PROGRAMS python/ptmrSim DESTINATION ${CMAKE_INSTALL_BINDIR})

