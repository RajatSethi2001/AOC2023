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

def solve(data, states, pos, steps, answers, maxSteps):
    if steps > maxSteps:
        return
    
    # if pos in states and steps in states[pos]:
    if pos in states and steps > states[pos]:
        return
    
    if data[pos[0] % len(data)][pos[1] % len(data[0])] == "#":
        return
    
    # if pos not in states:
    #     states[pos] = set()
    
    states[pos] = steps
    
    # if steps == maxSteps:
    #     # answers.add(pos)
    #     return

    # print(pos, steps)
    solve(data, states, (pos[0] + 1, pos[1]), steps + 1, answers, maxSteps)
    solve(data, states, (pos[0] - 1, pos[1]), steps + 1, answers, maxSteps)
    solve(data, states, (pos[0], pos[1] + 1), steps + 1, answers, maxSteps)
    solve(data, states, (pos[0], pos[1] - 1), steps + 1, answers, maxSteps)

def solution(data, maxSteps):
    answer = 0
    data = data.splitlines()
    start = None
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == 'S':
                start = (r, c)
                break
        if start is not None:
            break
    
    states = dict()
    answers = set()
    # states.add(start)
    solve(data, states, start, 0, answers, maxSteps)
    print(len(states))
    return str(sum([maxSteps % 2 == s % 2 for s in states.values()]))
    # return str(len(answers))

if part == 'a':
    example_data = open("examplea.txt", "r").read()
    # your_answer = solution(example_data)
    # print(f"Your attempt: {your_answer}")
    # print(f"Actual answer: {example_a_answer}")
    # # assert your_answer == example_a_answer

elif part == 'b':
    example_data = open("exampleb.txt", "r").read()
    your_answer = solution(example_data, 5000)
    print(f"Your attempt: {your_answer}")
    print(f"Actual answer: {example_b_answer}")
    assert your_answer == example_b_answer

# print(solution(puzzle_input, 26501365))
# submit(solution(puzzle_input), part=part, day=day, year=year)