from aocd import get_data, submit
from utils import *

part = 'a'
day = 25
year = 2023
example_a_answer = "54"
example_b_answer = ""

puzzle_input = get_data(day=day, year=year)

def getGroups(wires):
    nodeSet = set()
    groups = []
    for node in wires:
        if node not in nodeSet:
            group = set([node])
            nodeSet.add(node)

            nodeQ = [] + list(wires[node])
            while nodeQ:
                newNode = nodeQ.pop(0)
                if newNode not in group:
                    nodeSet.add(newNode)
                    group.add(newNode)

                    nodeQ += list(wires[newNode])
            groups.append(group)
    
    return groups
def getShort(contends):
    minCost = None
    minState = None
    for state, info in contends.items():
        if minCost is None or info[1] < minCost:
            minCost = info[1]
            minState = state
    
    return minState

def dijWire(start, wires):
    wins = dict()
    wins[start] = [None, 0]
    contends = dict()

    for connect in wires[start]:
        contends[connect] = [start, 1]
    
    while contends:
        winState = getShort(contends)
        wins[winState] = contends[winState]
        winCost = contends[winState][1]
    
        del contends[winState]

        for neighbor in wires[winState]:
            if neighbor not in wins:
                if neighbor not in contends or winCost + 1 < contends[neighbor][1]:
                    contends[neighbor] = [winState, winCost + 1]
    
    crosses = dict()
    for node in wins:
        currNode = node
        priorNode = wins[node][0]

        while priorNode is not None:
            # print(currNode, priorNode)
            cross = frozenset([currNode, priorNode])
            if cross not in crosses:
                crosses[cross] = 0
            crosses[cross] += 1

            currNode = priorNode
            priorNode = wins[currNode][0]
    
    return crosses

def solution(data):
    answer = 1
    data = data.splitlines()
    wires = dict()
    for line in data:
        wireData = line.split(": ")
        if wireData[0] not in wires:
            wires[wireData[0]] = set()

        wires[wireData[0]] = wires[wireData[0]].union(wireData[1].split(" "))
        for child in wires[wireData[0]]:
            if child not in wires:
                wires[child] = set()
             
            wires[child].add(wireData[0])
    
    allCrosses = dict()
    for wire in wires:
        crosses = dijWire(wire, wires)
        for cross, count in crosses.items():
            if cross not in allCrosses:
                allCrosses[cross] = 0
            allCrosses[cross] += count

    crossList = list(allCrosses.items())
    crossList.sort(key = lambda x: x[1], reverse=True)
    
    for cut in crossList[0:3]:
        cross = list(cut[0])
        node1 = cross[0]
        node2 = cross[1]

        wires[node1].remove(node2)
        wires[node2].remove(node1)
    
    groups = getGroups(wires)
    assert len(groups) == 2

    for group in groups:
        answer *= len(group)
    
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