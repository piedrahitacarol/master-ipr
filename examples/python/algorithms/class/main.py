#! /usr/bin/env python

FILE = "/home/jcgvicto/map1.csv"
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

init = Node(START_X, START_Y, 0, -2)
init.dump()
