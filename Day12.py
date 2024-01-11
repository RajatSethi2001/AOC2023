from aocd import get_data, submit
from utils import *
from collections import Counter
import os

part = 'b'
day = 12
year = 2023
example_a_answer = "21"
example_b_answer = "525152"

puzzle_input = get_data(day=day, year=year)

stateMap = dict()
def viable(springs, opNums):
    if not len(opNums):
        if "#" in springs:
            return 0
        # print(springs)
        return 1

    if sum(opNums) + len(opNums) - 1 > len(springs):
        return 0
    
    if sum(opNums) > springs.count("?") + springs.count("#"):
        return 0

    sols = 0
    op = opNums[0]
    otherNums = opNums[1::]

    for i in range(len(springs)):
        if springs[i] == '?' or springs[i] == '#':
            if not (i + op < len(springs) and springs[i + op] == "#") and not (i + op > len(springs)):
                valid = True
                
                if "#" in springs[:i]:
                    continue 

                for j in range(op):
                    if springs[i + j] == ".":
                        valid = False
                        break
                
                if valid:
                    # springs[:i].replace("?", ".") + "#" * op + 
                    newSprings = springs[i + op:]
                    
                    # if i + op < len(newSprings) and newSprings[i + op] == "?":
                    if len(newSprings) and newSprings[0] == "?":
                        newSprings = newSprings[1:]

                    # print(newSprings)
                    if (newSprings, otherNums) in stateMap:
                        sols += stateMap[(newSprings, otherNums)]
                    else:
                        solState = viable(newSprings, otherNums)
                        sols += solState
                        stateMap[(newSprings, otherNums)] = solState
    return sols
                    

def solution(data, save=False):
    data = data.splitlines()
    answer = 0
    index = 0

    if save and os.path.isfile("./Day12_Save.txt"):
        with open("./Day12_Save.txt", "r") as f:
            save_data = f.read().splitlines()[0].split(" ")
            index = int(save_data[0])
            answer = int(save_data[1])
    
    while index < len(data):
        line = data[index]
        line = line.split(" ")
        opNums = tuple([int(num) for num in line[1].split(",")] * 5)
        springs = (line[0] + "?") * 5
        springs = springs[:len(springs) - 1]

        sols = viable(springs, opNums)
        print(sols)
        answer += sols
        index += 1
        if save:
            with open("./Day12_Save.txt", "w") as f:
                f.write(f"{index} {answer}")
    
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

submit(solution(puzzle_input, True), part=part, day=day, year=year)