LoadYarp;  % yarp.matlab.LoadYarp

input_port = yarp.BufferedPortImageFloat;
input_port.open("/matlab/ecroSim/depthImage:i");
yarp.Network.connect("/ecroSim/depthImage:o", "/matlab/ecroSim/depthImage:i");

yarpImage=input_port.read;
h=yarpImage.height;
w=yarpImage.width;
%tool to convert the yarpImage (a Java object) into a matlab matrix
tool=YarpImageHelper(h, w);  % yarp.matlab.YarpImageHelper
A=tool.get2DMatrix(yarpImage);
%norm to visualize
normA = A - min(A(:));
normA = normA ./ max(normA(:)); % *
imshow(normA)
