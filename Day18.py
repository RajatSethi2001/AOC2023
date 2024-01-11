from aocd import get_data, submit
from utils import *
import sys
sys.setrecursionlimit(100000)

part = 'b'
day = 18
year = 2023
example_a_answer = "62"
example_b_answer = "952408144115"

puzzle_input = get_data(day=day, year=year)

def solution(data):
    answer = 0
    data = data.splitlines()
    x = 0
    y = 0
    dirs = ['R', 'D', 'L', 'U']

    horz = 0
    verts = 0
    corners = len(data)
    intVerts = 0

    ups = []
    downs = []
    downCors = []

    priorDir = None
    for line in data:
        inst = line.split(" ")
        color = inst[2]
        dir = int(color[-2])
        move = int(color[2:7], 16)

        # dir = dirs.index(inst[0])
        # move = int(inst[1])
        
        if dir == 1 or dir == 3:
            verts += move + 1
            if dir == 1:
                downs.append((x, y, y + move))
                if priorDir is not None and priorDir == 2:
                    downCors.append((x, y - 1, y + 1))
                y += move
            
            if dir == 3:
                ups.append((x, y, y - move))        
                y -= move
        
        else:
            horz += move + 1
            if dir == 0:
                if priorDir is not None and priorDir == 1:
                    downCors.append((x, y - 1, y + 1))
                x += move
            
            elif dir == 2:
                x -= move
        
        priorDir = dir
    
    downsList = downs + downCors
    downsList.sort(key = lambda x: x[0])

    upsList = ups
    upsList.sort(key = lambda x:x[0])

    for down in downsList:
        downX = down[0]
        downMin = down[1] + 1
        downMax = down[2] - 1

        downRanges = [(downMin, downMax)]
        while len(downRanges):
            chunk = downRanges.pop(0)
            chunkMin = chunk[0]
            chunkMax = chunk[1]

            if chunkMin > chunkMax:
                continue

            for up in upsList[::-1]:
                upX = up[0]
                upMin = up[2]
                upMax = up[1]

                if upX >= downX:
                    continue

                if upMin > upMax:
                    continue
                
                rectW = (downX - upX - 1)
                rectL = None

                if chunkMax < upMin or chunkMin > upMax:
                    continue

                if chunkMin < upMin and chunkMax > upMax:
                    rectL = (upMax - upMin + 1)
                    downRanges.append((chunkMin, upMin - 1))
                    downRanges.append((upMax + 1, chunkMax))
                
                elif chunkMin >= upMin and chunkMax <= upMax:
                    rectL = (chunkMax - chunkMin + 1)

                elif chunkMin < upMin and chunkMax >= upMin and chunkMax <= upMax:
                    rectL = (chunkMax - upMin + 1)
                    downRanges.append((chunkMin, upMin - 1))

                elif chunkMin >= upMin and chunkMin <= upMax and chunkMax > upMax:
                    rectL = (upMax - chunkMin + 1)
                    downRanges.append((upMax + 1, chunkMax))

                if rectL is not None:
                    rectA = rectW * rectL
                    intVerts += rectA 
                    break

    answer = horz + verts - corners + intVerts
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