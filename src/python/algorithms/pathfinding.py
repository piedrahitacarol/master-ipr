#! /usr/bin/env python

import argparse
import time
# 0: libre, 1: ocupado(muro/obstáculo), 2:visitado, 3:start, 4:goal

class Node:

    def __init__(self, x, y, my_id, parent_id, dist=100):
        self.x = x
        self.y = y
        self.my_id = my_id
        self.parent_id = parent_id
        self.dist = dist

    def dump(self):
        print("---------- x " + str(self.x) +
              " | y " + str(self.y) +
              " | id " + str(self.my_id) +
              " | parent id " + str(self.parent_id))

    def __lt__(self, neighbor):
        return self.dist < neighbor.dist

    def __eq__(self, node2):
        return self.x == node2.x and self.y == node2.y


def dump_map():
    for line in char_map:
        line = str(line)
        line = line.replace("0", '.').replace("1", "⊠") \
            .replace('[', '').replace(']', '').replace(',', '').replace('\'', '') \
            .replace('2', '#').replace('5', '♢') \
            .replace('3', '⊗').replace('4', '∅')
        print(line)


def breadth_fs(charMap, args):
    nodes = []
    visited = []

    init_node = Node(args.start_x, args.start_y, 0, -2)
    nodes.append(init_node)

    counter = 0
    while len(nodes) > 0:
        # take first node in list
        current_node = nodes.pop(0)
        current_node.dump()

        visited.append(current_node)

        x = current_node.x
        y = current_node.y
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for neighbor in neighbors:
            counter += 1
            if charMap[neighbor[0]][neighbor[1]] == '4':
                print("GOALLLL!!!")
                goal_parent_id = current_node.my_id
                return goal_parent_id, visited

            if charMap[neighbor[0]][neighbor[1]] == '2' or charMap[neighbor[0]][neighbor[1]] == '1':
                continue

            if charMap[neighbor[0]][neighbor[1]] == '0':
                print("mark visited")
                charMap[neighbor[0]][neighbor[1]] = '2'

                new_node = Node(neighbor[0], neighbor[1], counter, current_node.my_id)
                nodes.append(new_node)

        dump_map()


def depth_fs(charMap, args):
    nodes = []
    visited = []

    init_node = Node(args.start_x, args.start_y, 0, -2)
    nodes.append(init_node)

    counter = 0
    while len(nodes) > 0:
        # take last node in list
        current_node = nodes.pop(-1)
        current_node.dump()

        visited.append(current_node)

        x = current_node.x
        y = current_node.y
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for neighbor in neighbors:
            counter += 1
            if charMap[neighbor[0]][neighbor[1]] == '4':
                print("GOALLLL!!!")
                goal_parent_id = current_node.my_id
                return goal_parent_id, visited

            if charMap[neighbor[0]][neighbor[1]] == '2' or charMap[neighbor[0]][neighbor[1]] == '1':
                continue

            if charMap[neighbor[0]][neighbor[1]] == '0':
                print("mark visited")
                charMap[neighbor[0]][neighbor[1]] = '2'

                new_node = Node(neighbor[0], neighbor[1], counter, current_node.my_id)
                nodes.append(new_node)

        dump_map()


def best_fs(charMap, args):
    nodes = []
    closed = []

    # add initial node to list
    init_node = Node(args.start_x, args.start_y, 0, -2)
    end_node = Node(args.end_x, args.end_y, -1, -3)
    nodes.append(init_node)

    counter = 0
    while len(nodes) > 0:
        # put node with shortest distance to goal in the first place of list
        nodes.sort()
        # take that node and place it in closed list
        current_node = nodes.pop(0)
        closed.append(current_node)
        current_node.dump()

        # search 4 neighbors
        x = current_node.x
        y = current_node.y
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        n_nodes = []

        for neighbor in neighbors:
            counter += 1
            # goal found
            if charMap[neighbor[0]][neighbor[1]] == '4':
                print("GOALLLL!!!")
                goal_parent_id = current_node.my_id
                return goal_parent_id, closed

            if charMap[neighbor[0]][neighbor[1]] == '2' or charMap[neighbor[0]][neighbor[1]] == '1':
                continue

            # free coordinate
            if charMap[neighbor[0]][neighbor[1]] == '0':
                print("mark visited")
                charMap[neighbor[0]][neighbor[1]] = '2'

                # if neighbor is free, create node and calculate distance to end
                new_node = Node(neighbor[0], neighbor[1], counter, current_node.my_id)
                new_node.dist = abs(new_node.x - end_node.x) + abs(new_node.y - end_node.y)
            # place neighbor nodes in other list so we can compare them later
            n_nodes.append(new_node)

        # reorder neighbor nodes and add the one with shortest distance to list
        n_nodes.sort()
        nodes.append(n_nodes.pop(0))
        dump_map()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--map", type=str, default="/home/cpiedra/Descargas/master-ipr/map11/map11.csv", help="path to map")
    parser.add_argument("--start_x", type=int, default=5, help="start: coordinate x")
    parser.add_argument("--start_y", type=int, default=4, help="start: coordinate y")
    parser.add_argument("--end_x", type=int, default=13, help="end: coordinate x")
    parser.add_argument("--end_y", type=int, default=20, help="end: coordinate y")
    parser.add_argument("--algorithm", type=str, default="best", help="best/breadth/depth")
    args = parser.parse_args()
    print(args)

    char_map = []

    # read csv file to create map
    with open(args.map) as f:
        line = f.readline()
        while line:
            charLine = line.strip().split(',')
            char_map.append(charLine)
            line = f.readline()

    # mark start and end points in map
    char_map[args.start_x][args.start_y] = '3'
    char_map[args.end_x][args.end_y] = '4'

    # dump init map, choose algorithm, and calculate execution time
    dump_map()

    tic = time.time()
    if args.algorithm == 'best':
        goal_parent_id, nodes = best_fs(char_map, args)
    elif args.algorithm == 'breadth':
        goal_parent_id, nodes = breadth_fs(char_map, args)
    elif args.algorithm == 'depth':
        goal_parent_id, nodes = depth_fs(char_map, args)
    else:
        print("algorithm not supported")
    toc = time.time()

    # print final nodes and dump trajectory
    print("%%%%%%%%%%%%%%%%%%%")
    ok = False
    while not ok:
        for node in nodes:
            if node.my_id == goal_parent_id:
                node.dump()
                if not node.parent_id == -2:
                    char_map[node.x][node.y] = '5'
                goal_parent_id = node.parent_id
                if goal_parent_id == -2:
                    print("%%%%%%%%%%%%%%%%%")
                    ok = True

    dump_map()
    print("\nExecution time:", round((toc - tic)*1000, 3), 'ms')
