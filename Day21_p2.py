from aocd import get_data, submit
from utils import *
import sys
sys.setrecursionlimit(100000)

part = 'b'
day = 21
year = 2023
example_a_answer = ""
example_b_answer = "16"

puzzle_input = get_data(day=day, year=year)

def getPoints(data, start, maxSteps):
    states = dict()
    solve(data, states, start, 0, maxSteps)
    totalOdds = 0
    totalEvens = 0
    for key in states:
        if (key[0] + key[1]) % 2 == 0:
            totalEvens += 1
        else:
            totalOdds += 1
    
    return (totalOdds, totalEvens)

def solve(data, states, pos, steps, maxSteps):
    if not inBounds(data, pos):
        return
    
    if steps > maxSteps:
        return

    if pos in states and steps in states[pos]:
        return
    
    if data[pos[0]][pos[1]] == "#":
        return
    
    if pos not in states:
        states[pos] = set()
    
    states[pos].add(steps)
    
    solve(data, states, (pos[0] + 1, pos[1]), steps + 1, maxSteps)
    solve(data, states, (pos[0] - 1, pos[1]), steps + 1, maxSteps)
    solve(data, states, (pos[0], pos[1] + 1), steps + 1, maxSteps)
    solve(data, states, (pos[0], pos[1] - 1), steps + 1, maxSteps)

def solution(data, maxSteps):
    data = data.splitlines()
    start = None
    odds = 0
    evens = 0
    for r in range(len(data)):
        for c in range(len(data[r])):    
            if data[r][c] == 'S':
                start = (r, c)

    points = getPoints(data, start, 2 * len(data))
    print(points)
    odds = points[0]
    evens = points[1]

    blockRad = maxSteps // len(data)
    totalOdds = odds
    totalEvens = evens 

    print(blockRad)

    for n in range(1, blockRad):
        peri = 4 * n
        if n % 2 == 0:
            totalOdds += odds * peri
            totalEvens += evens * peri
        else:
            totalOdds += evens * peri
            totalEvens += odds * peri
    
    print(odds, evens)
    print(totalOdds, totalEvens)
    
    points = getPoints(data, (len(data) - 1, start[1]), len(data) - 1)
    print(points)
    totalOdds += points[0]
    totalEvens += points[1]

    points = getPoints(data, (0, start[1]), len(data) - 1)
    print(points)
    totalOdds += points[0]
    totalEvens += points[1]

    points = getPoints(data, (start[0], 0), len(data) - 1)
    print(points)
    totalOdds += points[0]
    totalEvens += points[1]
    
    points = getPoints(data, (start[0], len(data[0]) - 1), len(data) - 1)
    print(points)
    totalOdds += points[0]
    totalEvens += points[1]

    # Edges

    outPeri = blockRad * 4
    points = getPoints(data, (0, 0), len(data) - 1 + len(data) // 2)
    print(points)
    totalOdds += points[0] * ((outPeri - 4) // 4)
    totalEvens += points[1] * ((outPeri - 4) // 4)

    points = getPoints(data, (0, len(data[0]) - 1), len(data) - 1 + len(data) // 2)
    print(points)
    totalOdds += points[0] * ((outPeri - 4) // 4)
    totalEvens += points[1] * ((outPeri - 4) // 4)

    points = getPoints(data, (len(data) - 1, 0), len(data) - 1 + len(data) // 2)
    print(points)
    totalOdds += points[0] * ((outPeri - 4) // 4)
    totalEvens += points[1] * ((outPeri - 4) // 4)

    points = getPoints(data, (len(data) - 1, len(data[0]) - 1), len(data) - 1 + len(data) // 2)
    print(points)
    totalOdds += points[0] * ((outPeri - 4) // 4)
    totalEvens += points[1] * ((outPeri - 4) // 4)

    # Reverse Edges 
    points = getPoints(data, (0, 0), len(data) // 2 - 1)
    print(points)
    totalOdds += points[1] * (1 + (outPeri - 4) // 4)
    totalEvens += points[0] * (1 + (outPeri - 4) // 4)

    points = getPoints(data, (0, len(data[0]) - 1), len(data) // 2 - 1)
    print(points)
    totalOdds += points[1] * (1 + (outPeri - 4) // 4)
    totalEvens += points[0] * (1 + (outPeri - 4) // 4)

    points = getPoints(data, (len(data) - 1, 0), len(data) // 2 - 1)
    print(points)
    totalOdds += points[1] * (1 + (outPeri - 4) // 4)
    totalEvens += points[0] * (1 + (outPeri - 4) // 4)

    points = getPoints(data, (len(data) - 1, len(data[0]) - 1), len(data) // 2 - 1)
    print(points)
    totalOdds += points[1] * (1 + (outPeri - 4) // 4)
    totalEvens += points[0] * (1 + (outPeri - 4) // 4)

    print(totalOdds, totalEvens)
    
    if maxSteps % 2 == 0:
        answer = totalEvens
    else:
        answer = totalOdds
    
    return str(answer)

if part == 'a':
    example_data = open("examplea.txt", "r").read()
    # your_answer = solution(example_data)
    # print(f"Your attempt: {your_answer}")
    # print(f"Actual answer: {example_a_answer}")
    # # assert your_answer == example_a_answer

elif part == 'b':
    example_data = open("exampleb.txt", "r").read()
    # your_answer = solution(example_data, 5000)
    # print(f"Your attempt: {your_answer}")
    # print(f"Actual answer: {example_b_answer}")
    # assert your_answer == example_b_answer

submit(solution(puzzle_input, 26501365), part=part, day=day, year=year)