from aocd import get_data, submit
from utils import *
import sys
sys.setrecursionlimit(100000)

part = 'b'
day = 23
year = 2023
example_a_answer = "94"
example_b_answer = "154"

puzzle_input = get_data(day=day, year=year)

class Node:
    def __init__(self, pos):
        self.pos = pos
        self.neighbors = dict()

def isJunction(data, pos):
    exits = 0
    if inBounds(data, (pos[0] + 1, pos[1])) and data[pos[0] + 1][pos[1]] != "#":
        exits += 1
    
    if inBounds(data, (pos[0] - 1, pos[1])) and data[pos[0] - 1][pos[1]] != "#":
        exits += 1
    
    if inBounds(data, (pos[0], pos[1] + 1)) and data[pos[0]][pos[1] + 1] != "#":
        exits += 1
    
    if inBounds(data, (pos[0], pos[1] - 1)) and data[pos[0]][pos[1] - 1] != "#":
        exits += 1
    
    if exits != 2:
        return True
    
    return False

def getGraph(data, node, path, pos, dir, steps, nodeDict):
    if not inBounds(data, pos):
        return

    if data[pos[0]][pos[1]] == "#":
        return
    
    if isJunction(data, pos):
        if pos in nodeDict:
            existNeighbor = nodeDict[pos]
            if node.pos in existNeighbor.neighbors:
                if steps > existNeighbor.neighbors[node.pos]:
                    existNeighbor.neighbors[node.pos] = steps
                    node.neighbors[pos] = steps
            else:
                existNeighbor.neighbors[node.pos] = steps
                node.neighbors[pos] = steps
            return

        newNode = Node(pos)
        nodeDict[pos] = newNode
        node.neighbors[pos] = steps
        newNode.neighbors[node.pos] = steps
        
        if dir != 'd':
            path.add(pos)
            getGraph(data, newNode, path, (pos[0] - 1, pos[1]), 'u', 1, nodeDict)
            path.remove(pos)
        if dir != 'u':
            path.add(pos)
            getGraph(data, newNode, path, (pos[0] + 1, pos[1]), 'd', 1, nodeDict)
            path.remove(pos)
        if dir != 'r':
            path.add(pos)
            getGraph(data, newNode, path, (pos[0], pos[1] - 1), 'l', 1, nodeDict)
            path.remove(pos)
        if dir != 'l':
            path.add(pos)
            getGraph(data, newNode, path, (pos[0], pos[1] + 1), 'r', 1, nodeDict)
            path.remove(pos)
    
    else:
        if dir != 'd':
            getGraph(data, node, path, (pos[0] - 1, pos[1]), 'u', steps + 1, nodeDict)
        if dir != 'u':
            getGraph(data, node, path, (pos[0] + 1, pos[1]), 'd', steps + 1, nodeDict)
        if dir != 'r':
            getGraph(data, node, path, (pos[0], pos[1] - 1), 'l', steps + 1, nodeDict)
        if dir != 'l':
            getGraph(data, node, path, (pos[0], pos[1] + 1), 'r', steps + 1, nodeDict)

def getGraphHelp(data):
    startPos = (0, 1)
    startPath = set()
    startPath.add(startPos)
    startNode = Node(startPos)
    nodeDict = dict()
    nodeDict[startPos] = startNode
    
    getGraph(data, startNode, startPath, (1, 1), 'd', 1, nodeDict)
   
    return startNode, nodeDict

def graphTrav(node, path, cost, nodeDict, answers):
    if node.pos in path:
        return
    
    if node.pos in answers:
        if cost > answers[node.pos]:
            answers[node.pos] = cost
    else:
        answers[node.pos] = cost
    
    for neighborPos, neighborCost in node.neighbors.items():
        path.add(node.pos)
        graphTrav(nodeDict[neighborPos], path, cost + neighborCost, nodeDict, answers)
        path.remove(node.pos)


def solution(data):
    answer = 0
    data = data.splitlines()
    graph, nodeDict = getGraphHelp(data)

    nodeQ = [graph]
    printedNodes = set()
    while nodeQ:
        node = nodeQ.pop(0)
        if node.pos in printedNodes:
            continue
        printedNodes.add(node.pos)
        print(f"Node at {node.pos}")
        for neighborPos, neighborCost in node.neighbors.items():
            neighborNode = nodeDict[neighborPos]
            print(f"Neighbor at {neighborPos} with cost of {neighborCost}")
            nodeQ.append(neighborNode)

        print()
    
    answers = dict()
    graphTrav(graph, set(), 0, nodeDict, answers)
    answer = answers[(len(data) - 1, len(data[0]) - 2)]
    
    return str(answer)

if part == 'a':
    example_data = open("examplea.txt", "r").read()
    your_answer = solution(example_data)
    print(f"Your attempt: {your_answer}")
    print(f"Actual answer: {example_a_answer}")
    assert your_answer == example_a_answer

elif part == 'b':
    example_data = open("exampleb.txt", "r").read()
    your_answer = solution(example_data)
    print(f"Your attempt: {your_answer}")
    print(f"Actual answer: {example_b_answer}")
    assert your_answer == example_b_answer

submit(solution(puzzle_input), part=part, day=day, year=year)