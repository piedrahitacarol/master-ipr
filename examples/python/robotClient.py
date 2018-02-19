#! /usr/bin/env python

import yarp
import asrob_yarp_devices

yarp.Network.init()

if not yarp.Network.checkNetwork():
    print "[error] Please try running yarp server"
    quit()

robotOptions = yarp.Property()
robotOptions.put('device','RobotClient')
robotOptions.put('name','/ecroSim')
robotDevice = yarp.PolyDriver(robotOptions)  # calls open -> connects

robot = asrob_yarp_devices.viewIRobotManager(robotDevice)  # view the actual interface

print "moveForward(3)"
robot.moveForward(3)

print "delay(3)"
yarp.Time.delay(3)  # delay in [seconds]

print "robot.turnRight(3)"
robot.turnRight(3)

print "delay(5)"
yarp.Time.delay(5)  # delay in [seconds]

print "moveForward(3)"
robot.moveForward(3)

print "delay(3)"
yarp.Time.delay(3)  # delay in [seconds]

print "stopMovement()"
robot.stopMovement()

robotDevice.close()
