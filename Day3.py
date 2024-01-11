from aocd import get_data, get_examples, submit
from utils import *

part = 'b'
day = 3
year = 2023

def solution(data):
    answer = 0
    data = data.splitlines()
    gears = {}
    for lineIndex in range(len(data)):
        line = data[lineIndex]
        currNum = ""
        indexStart = None

        for i in range(len(line)):
            if line[i].isdigit():
                currNum += line[i]
                if indexStart is None:
                    indexStart = i
            
            if indexStart is not None and (not line[i].isdigit() or i == len(line) - 1):
                part = False
                gearSet = set()
                for charIndex in range(indexStart, i):
                    for r in range(-1, 2):
                        for c in range(-1, 2):
                            if lineIndex + r >= 0 and lineIndex + r < len(data) and charIndex + c >= 0 and charIndex + c < len(line) and data[lineIndex + r][charIndex + c] == "*":
                                gearSet.add((lineIndex + r, charIndex + c))
                
                for gear in gearSet:
                    if gear in gears:
                        gears[gear].append(currNum)
                    else:
                        gears[gear] = [currNum]
                
                currNum = ""
                indexStart = None

    print(gears)
    for gear in gears:
        if len(gears[gear]) == 2:
            answer += int(gears[gear][0]) * int(gears[gear][1])
    
    print(answer)                
    return str(answer)

puzzle_input = get_data(day=day, year=year)
example = get_examples(day=day, year=year)[0]

if part == 'a':
    example_data = example.input_data
    your_answer = solution(example_data)
    print(f"Your attempt: {your_answer}")
    print(f"Actual answer: {example.answer_a}")
    if example.answer_a is not None:
        assert your_answer == example.answer_a

elif part == 'b':
    example_data = open("exampleb.txt", "r").read()
    your_answer = solution(example_data)
    print(f"Your attempt: {your_answer}")
    print(f"Actual answer: {example.answer_b}")
    if example.answer_b is not None:
        assert your_answer == example.answer_b

solution(puzzle_input)
submit(solution(puzzle_input), part=part, day=day, year=year)