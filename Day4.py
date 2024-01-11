from aocd import get_data, submit
from utils import *

part = 'b'
day = 4
year = 2023
example_a_answer = "13"
example_b_answer = "30"

puzzle_input = get_data(day=day, year=year)

def solution(data):
    answer = 0
    data = data.splitlines()
    matches = []
    index = 0
    for line in data:
        line = line.split(": ")[1]
        winners = set(line.split(" | ")[0].split(" "))
        picks = set(line.split(" | ")[1].split(" "))
        
        try:
            winners.remove('')
        except:
            pass

        try:
            picks.remove('')
        except:
            pass

        points = 0
        for pick in picks:
            if pick in winners and pick != "":
                points += 1
        
        matches.append(points)
        index += 1

    print(matches)
    copies = {}
    for cardIndex in range(len(matches) - 1, -1, -1):
        wins = matches[cardIndex]
        copy = 1
        for w in range(wins):
            copy += copies[cardIndex + w + 1]
        copies[cardIndex] = copy
    
    return str(sum(copies.values()))

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