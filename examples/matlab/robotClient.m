LoadYarp;  % yarp.matlab.LoadYarp

robotClient = yarp.Port;
robotClient.open('/matlab/ecroSim/rpc:c');
yarp.Network.connect('/matlab/ecroSim/rpc:c','/ecroSim/rpc:s');


disp 'moveForward(3)'
b = yarp.Bottle;
b.addVocab( yarp.Vocab.encode('movf') );
b.addDouble(3.0);
robotClient.write(b);

disp 'delay(3)'
pause(3);

disp 'turnRight(3)'
b.clear();
b.addVocab( yarp.Vocab.encode('trnr') );
b.addDouble(3.0);
robotClient.write(b);

disp 'delay(5)'
pause(5);

disp 'moveForward(3)'
b.clear();
b.addVocab( yarp.Vocab.encode('movf') );
b.addDouble(3.0);
robotClient.write(b);

disp 'delay(3)'
pause(3);

disp 'stopMovement()'
b.clear();
b.addVocab( yarp.Vocab.encode('stpm') );
robotClient.write(b);

robotClient.close();
