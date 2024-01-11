from aocd import get_data, submit
from utils import *

import sys
sys.setrecursionlimit(100000)

part = 'b'
day = 10
year = 2023
example_a_answer = "4"
example_b_answer = "8"

puzzle_input = get_data(day=day, year=year)

def traverse(data, start, startPipe, currPos, lastPos, states):
    if not inBounds(data, currPos):
        return False
    
    if currPos in states:
        return False
    
    currInst = data[currPos[0]][currPos[1]]
    if currPos == start:
        currInst = startPipe

    if currInst == ".":
        return False
    
    states.append(currPos)
    rowDiff = lastPos[0] - currPos[0]
    colDiff = lastPos[1] - currPos[1]

    dir = None
    if rowDiff == 0 and colDiff == 1:
        dir = "left"
    elif rowDiff == 0 and colDiff == -1:
        dir = "right"
    elif rowDiff == 1 and colDiff == 0:
        dir = "up"
    elif rowDiff == -1 and colDiff == 0:
        dir = "down"
    else:
        return False
    
    newInst = None
    if currInst == "F":
        if dir == "up":
            newInst = "right"
        elif dir == "left":
            newInst = "down"
        else:
            return False
    elif currInst == "J":
        if dir == "right":
            newInst = "up"
        elif dir == "down":
            newInst = "left"
        else:
            return False
    elif currInst == "7":
        if dir == "right":
            newInst = "down"
        elif dir == "up":
            newInst = "left"
        else:
            return False
    elif currInst == "L":
        if dir == "down":
            newInst = "right"
        elif dir == "left":
            newInst = "up"
        else:
            return False
    elif currInst == "-":
        if dir == "left":
            newInst = "left"
        elif dir == "right":
            newInst = "right"
        else:
            return False      
    elif currInst == "|":
        if dir == "up":
            newInst = "up"
        elif dir == "down":
            newInst = "down"
        else:
            return False   
    else:
        return False

    if currPos == start:
        return True
    
    nextPos = None
    if newInst == "up":
        nextPos = (currPos[0] - 1, currPos[1])
    elif newInst == "down":
        nextPos = (currPos[0] + 1, currPos[1])
    elif newInst == "right":
        nextPos = (currPos[0], currPos[1] + 1)
    elif newInst == "left":
        nextPos = (currPos[0], currPos[1] - 1)
    else:
        return False

    return traverse(data, start, startPipe, nextPos, currPos, states)

def getGroup(data, pipeStates, pos, group):
    if not inBounds(data, pos):
        return
    
    if pos in group:
        return
    
    if pos in pipeStates:
        return
    
    group.add(pos)

    getGroup(data, pipeStates, (pos[0], pos[1] - 1), group)
    getGroup(data, pipeStates, (pos[0] - 1, pos[1]), group)
    getGroup(data, pipeStates, (pos[0] + 1, pos[1]), group)
    getGroup(data, pipeStates, (pos[0], pos[1] + 1), group)
    

def solution(data):
    data = data.splitlines()
    start = None
    for i in range(len(data)):
        if data[i].find('S') != -1:
            start = (i, data[i].find('S'))
            break

    starts = ['|', '-', 'L', 'F', 'J', '7']
    answer = None
    trueStates = []
    success = False
    for pipe in starts:
        startDir = None
        if pipe == "|":
            startDir = ("up", "down")
        elif pipe == "-":
            startDir = ("left", "right")
        elif pipe == "F":
            startDir = ("down", "right")
        elif pipe == "L":
            startDir = ("up", "right")
        elif pipe == "J":
            startDir = ("left", "up")
        elif pipe == "7":
            startDir = ("left", "down")
        
        for dir in startDir:
            states = []
            if dir == "up":
                nextPos = (start[0] - 1, start[1])
            elif dir == "down":
                nextPos = (start[0] + 1, start[1])
            elif dir == "right":
                nextPos = (start[0], start[1] + 1)
            elif dir == "left":
                nextPos = (start[0], start[1] - 1)
            else:
                return False
            
            success = traverse(data, start, pipe, nextPos, start, states)
            if success:
                data[start[0]] = data[start[0]].replace('S', pipe)
                trueStates = states
                break
                # for state in states:
                #     if state not in trueStates or states[state] < trueStates[state]:
                #         trueStates[state] = states[state]

        if success:
            break
    # del trueStates[start]
    # answer = max(trueStates.values())

    startPos = None
    for pos in trueStates:
        if data[pos[0]][pos[1]] == "-":
            startPos = pos
            break
    
    rotations = ["right", "down", "left", "up"]
    currDir = 0

    currPos = startPos
    loop = False

    sides = set()
    while not loop:
        newPos = None
        currPoint = (currDir - 1) % len(rotations)
        if rotations[currPoint] == "up":
            newPos = (currPos[0] - 1, currPos[1])
        elif rotations[currPoint] == "down":
            newPos = (currPos[0] + 1, currPos[1])
        elif rotations[currPoint] == "left":
            newPos = (currPos[0], currPos[1] - 1)
        elif rotations[currPoint] == "right":
            newPos = (currPos[0], currPos[1] + 1)
        else:
            raise Exception(f"Error: currPoint is {rotations[currPoint]}")
        
        if inBounds(data, newPos) and newPos not in trueStates:
            sides.add(newPos)
        
        nextPos = None
        if rotations[currDir] == "up":
            nextPos = (currPos[0] - 1, currPos[1])
        elif rotations[currDir] == "down":
            nextPos = (currPos[0] + 1, currPos[1])
        elif rotations[currDir] == "left":
            nextPos = (currPos[0], currPos[1] - 1)
        elif rotations[currDir] == "right":
            nextPos = (currPos[0], currPos[1] + 1)
        
        nextInst = data[nextPos[0]][nextPos[1]]
        extraAdd = []
        if nextInst == "F":
            if rotations[currDir] == "up":
                currDir += 1
                extraAdd.append((nextPos[0], nextPos[1] - 1))
                extraAdd.append((nextPos[0] - 1, nextPos[1] - 1))
                extraAdd.append((nextPos[0] - 1, nextPos[1]))
            elif rotations[currDir] == "left":
                currDir -= 1
                
        
        elif nextInst == "L":
            if rotations[currDir] == "left":
                currDir += 1
                extraAdd.append((nextPos[0] + 1, nextPos[1]))
                extraAdd.append((nextPos[0] + 1, nextPos[1] - 1))
                extraAdd.append((nextPos[0], nextPos[1] - 1))
            elif rotations[currDir] == "down":
                currDir -= 1
                
        
        elif nextInst == "7":
            if rotations[currDir] == "right":
                currDir += 1
                extraAdd.append((nextPos[0] - 1, nextPos[1]))
                extraAdd.append((nextPos[0] - 1, nextPos[1] + 1))
                extraAdd.append((nextPos[0], nextPos[1] + 1))
            elif rotations[currDir] == "up":
                currDir -= 1
                
        
        elif nextInst == "J":
            if rotations[currDir] == "down":
                currDir += 1
                extraAdd.append((nextPos[0], nextPos[1] + 1))
                extraAdd.append((nextPos[0] - 1, nextPos[1] - 1))
                extraAdd.append((nextPos[0] - 1, nextPos[1]))
            elif rotations[currDir] == "right":
                currDir -= 1
                
        
        currDir = currDir % len(rotations)
        if extraAdd is not None and inBounds(data, extraAdd) and extraAdd not in trueStates:
            sides.add(nextPos)
        
        currPos = nextPos

        if currPos == startPos:
            loop = True

    newSides = set()
    for point in sides:
        tempSides = set()
        getGroup(data, trueStates, point, tempSides)
        newSides = newSides.union(tempSides)

    enclosed = True
    for point in newSides:
        if point[0] == 0 or point[0] == len(data) - 1 or point[1] == 0 or point[1] == len(data[point[0]]) - 1:
            enclosed = False
            break
    
    print(len(newSides))
    print(len(data) * len(data[0]) - len(newSides) - len(trueStates))
    print(len(data) * len(data[0]))
    print(len(trueStates))
    answer = 0
    if enclosed:
        answer = len(newSides)
    else:
        answer = len(data) * len(data[0]) - len(newSides) - len(trueStates)

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

print(solution(puzzle_input))
# submit(solution(puzzle_input), part=part, day=day, year=year)