from aocd import get_data, submit
from utils import *
import math

part = 'b'
day = 8
year = 2023
example_a_answer = "6"
example_b_answer = "6"

puzzle_input = get_data(day=day, year=year)

def solution(data):
    data = data.splitlines()
    inst = data[0]
    maps = data[2::]

    leftRight = {}
    for line in maps:
        line = line.split(" = ")
        nodes = line[1].replace("(", "").replace(")","").split(", ")
        leftRight[line[0]] = nodes
    
    answer = 0
    nodes = []
    for key in leftRight:
        if key[-1] == 'A':
            nodes.append(key)
    
    nodeZ = []
    for node in nodes:
        endNode = node
        index = 0
        firstZ = None
        secondZ = None
        while secondZ is None:
            if endNode[-1] == 'Z':
                if firstZ is None:
                    firstZ = index
                else:
                    secondZ = index
                    break
            ins = inst[index % len(inst)]
            index += 1
            if ins == 'L':
                endNode = leftRight[endNode][0]
            else:
                endNode = leftRight[endNode][1]

        nodeZ.append((secondZ - firstZ, firstZ))
    
    answer = math.lcm(*[node[1] for node in nodeZ])
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