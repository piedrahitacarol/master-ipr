LoadYarp;

input_port = yarp.Port;
input_port.open("/matlab/ecroSim/depthImage:i");
yarp.Network.connect("/ecroSim/depthImage:o", "/matlab/ecroSim/depthImage:i");

height = 96;
width = 128;
