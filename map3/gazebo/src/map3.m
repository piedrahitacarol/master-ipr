% Connect to VM ros master (roscore)
ipaddress = '192.168.179.128'
rosinit(ipaddress,'NodeHost','192.168.179.1')

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
bookshelf = ExampleHelperGazeboModel('bookshelf','gazeboDB');

% place botmodel
bot = spawnModel(gazebo,botmodel,[-1.5 1.5 0])
% place walls
spawnModel(gazebo,wall,[-7.5 0 0],[0,0,pi/2])
spawnModel(gazebo,wall,[-3.75 3.75 0])
spawnModel(gazebo,wall,[3.75 3.75 0])
spawnModel(gazebo,wall,[-3.75 -3.75 0])
spawnModel(gazebo,wall,[3.75 -3.75 0])
spawnModel(gazebo,wall,[7.5 0 0],[0,0,pi/2])
% place barriers
spawnModel(gazebo,barrier,[0 1.8 0],[0,0,pi/2])

spawnModel(gazebo,barrier,[-1.8 0 0])
spawnModel(gazebo,barrier,[1.8 0 0])

spawnModel(gazebo,barrier,[-4 0 0])
spawnModel(gazebo,barrier,[4 0 0])

spawnModel(gazebo,barrier,[-3 0 0],[0 0 pi/2])
spawnModel(gazebo,barrier,[3 0 0],[0 0 pi/2])

% place bookshelves
spawnModel(gazebo,bookshelf,[-5.5 -2 0],[0 0 pi/8])
spawnModel(gazebo,bookshelf,[5.5 -2 0],[0 0 pi/8])

% (check target)
%bot = spawnModel(gazebo,botmodel,[1.5 1.5 0])

% Close connection with VM ros master
rosshutdown
