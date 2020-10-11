# Copyright: 2014 UC3M
# Author: Juan G Victores
# CopyPolicy: Released under the terms of the GNU GPL v2.0.

set(appname openrave)

file(GLOB xml ${CMAKE_CURRENT_SOURCE_DIR}/*.xml)
file(GLOB ecro ${CMAKE_CURRENT_SOURCE_DIR}/ecro/*.xml)
file(GLOB ecro/models ${CMAKE_CURRENT_SOURCE_DIR}/ecro/models/*.wrl)

yarp_install(FILES ${xml} DESTINATION ${MASTER-IPR_CONTEXTS_INSTALL_DIR}/${appname})
yarp_install(FILES ${ecro} DESTINATION ${MASTER-IPR_CONTEXTS_INSTALL_DIR}/${appname}/ecro)
yarp_install(FILES ${ecro/models} DESTINATION ${MASTER-IPR_CONTEXTS_INSTALL_DIR}/${appname}/ecro/models)
yarp_install(PROGRAMS iprSim10 DESTINATION ${CMAKE_INSTALL_BINDIR})
