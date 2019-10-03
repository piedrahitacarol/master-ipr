#! /usr/bin/env python

FILE_NAME = "/home/jcgvicto/map1.csv"
START_X = 2
START_Y = 2
END_X = 7
END_Y = 2

class Node:
    def __init__(self, x, y, myId, parentId):
        self.x = x
        self.y = y
        self.myId = myId
        self.parentId = parentId
    def dump(self):
        print("---------- x "+str(self.x)+\
                         " | y "+str(self.y)+\
                         " | id "+str(self.myId)+\
                         " | parentId "+str(self.parentId))

nodes = []

init = Node(START_X, START_Y, 0, -2)
# init.dump()

nodes.append(init)

charMap = []

def dumpMap():
    for line in charMap:
        print line

with open(FILE_NAME) as f:
    line = f.readline()
    while line:
        charLine = line.strip().split(',')
        charMap.append(charLine)
        line = f.readline()

charMap[START_X][START_Y] = '3'
charMap[END_X][END_Y] = '4'

dumpMap()

done = False
goalParentId = -1

while not done:
    print("--------------------- number of nodes: "+str(len(nodes)))
    for node in nodes:
        node.dump()

    break
