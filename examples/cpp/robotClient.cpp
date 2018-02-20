#include <yarp/os/all.h>
#include <yarp/dev/all.h>

#include "IRobotManager.hpp" // we need this to work with the RobotClient device

int main(int argc, char *argv[])
{
    yarp::os::Network yarp;

    if (!yarp::os::Network::checkNetwork())
    {
        printf("Please start a yarp name server first\n");
        return 1;
    }

    yarp::os::Property options;
    options.put("device", "RobotClient"); // our device (a dynamically loaded library)
    options.put("name", "/ecroSim"); // remote port through which we'll talk to the server

    yarp::dev::PolyDriver dd;
    if ( ! dd.open(options) )
    {
        printf("Device not available.\n");
        dd.close();
        return 1;
    }

    asrob::IRobotManager *robot;

    if (!dd.view(robot))
    {
        printf("[error] Problems acquiring interface\n");
        dd.close();
        return 1;
    }
    printf("[success] acquired motor interface\n");

    robot->moveForward(1);

    dd.close();

    return 0;
}
