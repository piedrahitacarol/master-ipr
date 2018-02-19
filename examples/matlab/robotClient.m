LoadYarp;  % yarp.matlab.LoadYarp

port = yarp.Port;
port.open('/matlab/ecroSim/rpc:c');
yarp.Network.connect('/matlab/ecroSim/rpc:c','/ecroSim/rpc:s');

b = yarp.Bottle;
b.addVocab(yarp.Vocab.encode('movf'));
b.addDouble(3.0);
port.write(b);

