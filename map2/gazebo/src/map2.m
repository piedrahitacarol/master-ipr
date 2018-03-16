% help: https://es.mathworks.com/help/robotics/examples/add-build-and-remove-objects-in-gazebo.html

% Connect to VM ros master (roscore)
ipaddress = '192.168.179.128'  % ipaddress = 'localhost'
rosinit(ipaddress,'NodeHost','192.168.179.1')  % rosinit(ipaddress)

% Connect to VM gazebo instance
gazebo = ExampleHelperGazeboCommunicator();

% See if any model is loaded
list = getSpawnedModels(gazebo)
% Remove it (moving around not too good, better erase and create new where we want it)
removeModel(gazebo,'mobile_base');

% see all possible models
builtInModels = exampleHelperGazeboListModels()

% load some useful models
botmodel = ExampleHelperGazeboModel('turtlebot','gazeboDB');
wall = ExampleHelperGazeboModel('grey_wall','gazeboDB');
barrier = ExampleHelperGazeboModel('jersey_barrier','gazeboDB');

% place botmodel
bot = spawnModel(gazebo,botmodel,[-3 3 0])
% place walls
spawnModel(gazebo,wall,[-3.75 0 0],[0 0 pi/2])
spawnModel(gazebo,wall,[0 3.75 0])
spawnModel(gazebo,wall,[0 -3.75 0])
spawnModel(gazebo,wall,[3.75 0 0],[0 0 pi/2])
% place barriers
spawnModel(gazebo,barrier,[-1.8 1.5 0])
spawnModel(gazebo,barrier,[1.8 -1.5 0])

% (check target)
%bot = spawnModel(gazebo,botmodel,[3 -3 0])

% Close connection with VM ros master
rosshutdown
