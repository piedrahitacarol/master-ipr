cmake_minimum_required(VERSION 2.8.0)

# Start a project.
project(depthClient)

find_package(YARP REQUIRED COMPONENTS os dev sig)

# Set up our main executables.

add_executable(depthClient depthClient.cpp)

target_link_libraries(depthClient YARP::YARP_OS
                                  YARP::YARP_init
                                  YARP::YARP_dev)

include(GNUInstallDirs)

install(TARGETS depthClient
        DESTINATION ${CMAKE_INSTALL_BINDIR})
