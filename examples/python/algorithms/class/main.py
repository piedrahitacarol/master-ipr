#! /usr/bin/env python

DEFAULT_FILE = "/home/jcgvicto/map1.csv"
DEFAULT_START_X = 2
DEFAULT_START_Y = 2
DEFAULT_END_X = 7
DEFAULT_END_Y = 2

class Node:
    def __init__(self, x, y, myId, parentId):
        self.x = x
        self.y = y
        self.myId = myId
        self.parentId = parentId
