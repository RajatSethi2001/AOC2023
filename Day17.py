from aocd import get_data, submit
from utils import *

part = 'b'
day = 17
year = 2023
example_a_answer = "102"
example_b_answer = "94"

puzzle_input = get_data(day=day, year=year)

dirs = ['u', 'r', 'd', 'l']

def getNext(data, point, dir, forwards, cost):
    dirChar = dirs[dir]
    pointNewR = None
    pointNewC = None
    if dirChar == 'u':
        pointNewR = point[0] - 1
        pointNewC = point[1]
    elif dirChar == 'r':
        pointNewR = point[0]
        pointNewC = point[1] + 1
    elif dirChar == 'd':
        pointNewR = point[0] + 1
        pointNewC = point[1]
    elif dirChar == 'l':
        pointNewR = point[0]
        pointNewC = point[1] - 1
    
    pointNew = (pointNewR, pointNewC)
    if inBounds(data, pointNew) and forwards <= 10:
        return (pointNew, dir, forwards, cost + int(data[pointNewR][pointNewC]))
    return ()

def lavaDij(data, point, dir, forwards, cost):
    states = set()
    dirLeft = (dir - 1) % len(dirs)
    dirRight = (dir + 1) % len(dirs)

    states.add(getNext(data, point, dir, forwards + 1, cost))
    if forwards >= 4 or cost == 0:
        states.add(getNext(data, point, dirLeft, 1, cost))
        states.add(getNext(data, point, dirRight, 1, cost))

    if () in states:
        states.remove(())
    
    return states

def lavaDijHelp(data):
    currState = ((0, 0), 1, 0, 0)
    contendDict = dict()
    states = dict()

    goal = (len(data) - 1, len(data[len(data) - 1]) - 1)
    while currState[0] != goal:
        nextStates = lavaDij(data, currState[0], currState[1], currState[2], currState[3])
        for s in nextStates:
            if s[:3] not in states and (s[:3] not in contendDict or s[3] < contendDict[s[:3]]):
                if s[0] != goal or s[2] >= 4:
                    contendDict[s[:3]] = s[3]

        states[currState[:3]] = currState[2]
        contendQ = list(contendDict.items())
        contendQ.sort(key=lambda x:x[1])
        # print(contendQ)

        bestState = contendQ.pop(0)
        contendDict.pop(bestState[0])
        currState = bestState[0] + (bestState[1],)
    
        print(currState[3])
    return currState[3]

def solution(data):
    data = data.splitlines()
    answer = lavaDijHelp(data)
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