from aocd import get_data, submit
from utils import *
import re

part = 'b'
day = 6
year = 2023
example_a_answer = "288"
example_b_answer = "71503"

puzzle_input = get_data(day=day, year=year)

def solution(data):
    data = data.splitlines()
    data = [re.sub(' +', ' ', line).split(": ")[1] for line in data]
    for index in range(len(data)):
        data[index] = int(data[index].replace(" ", ""))
    
    races = [(data[0], data[1])]
    # for index in range(len(data[0])):
    #     races.append((data[0][index], data[1][index]))
    
    print(races)
    answer = 1
    for race in races:
        dur = race[0]
        dist = race[1]

        wins = 0
        for button in range(dur + 1):
            if button * (dur - button) > dist:
                wins += 1
        answer *= wins
    
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