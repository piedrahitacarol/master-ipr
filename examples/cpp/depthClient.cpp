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

    yarp::os::Port port;
    port.open("/cpp/ecroSim/depthImage:i");
    yarp::os::Network::connect("/ecroSim/depthImage:o","/cpp/ecroSim/depthImage:i");

    port.close();

    return 0;
}
