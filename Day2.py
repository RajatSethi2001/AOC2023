from aocd import get_data, get_examples, submit
from utils import *

part = 'b'
day = 2
year = 2023

puzzle_input = get_data(day=day, year=year)
example = get_examples(day=day, year=year)[0]
example_data = example.input_data
# example_data = open("input.txt", "r").read()

def solution(data):
    data = data.splitlines()
    answer = 0
    for game in data:
        game = game.split(": ")[1]
        rounds = game.split("; ")
        marbles = [round.split(", ") for round in rounds]
        
        maxes = {}
        for round in marbles:
            for marble in round:
                pick = marble.split(" ")
                count = int(pick[0])
                color = pick[1]
        
                if color not in maxes or count > maxes[color]:
                    maxes[color] = count
        
        power = 1
        for key in maxes:
            power *= maxes[key]

        answer += power
        
    return str(answer)

example_answer = solution(example_data)
print(f"Your attempt: {example_answer}")
if part == 'a':
    print(f"Actual answer: {example.answer_a}")
    assert example_answer == example.answer_a
elif part == 'b':
    print(f"Actual answer: {example.answer_b}")
    assert example_answer == example.answer_b
else:
    raise Exception(f"Part {part} does not exist")

submit(solution(puzzle_input), part=part, day=day, year=year)