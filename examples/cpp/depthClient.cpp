#include <yarp/os/all.h>
#include <yarp/dev/all.h>

int main(int argc, char *argv[])
{
    yarp::os::Network yarp;

    if (!yarp::os::Network::checkNetwork())
    {
        printf("Please start a yarp name server first\n");
        return 1;
    }

    /*yarp::os::Property robotOptions;
    robotOptions.put("device", "RobotClient"); // our device (a dynamically loaded library)
    robotOptions.put("name", "/ecroSim"); // remote port through which we'll talk to the server

    yarp::dev::PolyDriver robotDevice;
    if ( ! robotDevice.open(robotOptions) )
    {
        printf("Device not available.\n");
        robotDevice.close();
        return 1;
    }

    asrob::IRobotManager *robot;

    if ( ! robotDevice.view(robot) )
    {
        printf("[error] Problems acquiring interface\n");
        robotDevice.close();
        return 1;
    }
    printf("[success] acquired motor interface\n");

    printf("moveForward(3)\n");
    robot->moveForward(3);

    printf("delay(3)\n");
    yarp::os::Time::delay(3);  // delay in [seconds]

    printf("robot.turnRight(3)\n");
    robot->turnRight(3);

    printf("delay(5)\n");
    yarp::os::Time::delay(5);  // delay in [seconds]

    printf("moveForward(3)\n");
    robot->moveForward(3);

    printf("delay(3)\n");
    yarp::os::Time::delay(3);  // delay in [seconds]

    printf("stopMovement()\n");
    robot->stopMovement();

    robotDevice.close();*/

    return 0;
}
