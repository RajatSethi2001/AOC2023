from aocd import get_data, submit
from utils import *
import copy
import sys
sys.setrecursionlimit(100000)
import gc

part = 'b'
day = 23
year = 2023
example_a_answer = "94"
example_b_answer = "154"

puzzle_input = get_data(day=day, year=year)

def path(data, states, state, pos, dir, steps, answer):
    if not inBounds(data, pos):
        return

    if data[pos[0]][pos[1]] == "#":
        return

    # if data[pos[0]][pos[1]] == ">" and dir != 'r':
    #     return
    
    # if data[pos[0]][pos[1]] == "v" and dir != 'd':
    #     return
    
    # if data[pos[0]][pos[1]] == "<" and dir != 'l':
    #     return
    
    # if data[pos[0]][pos[1]] == "^" and dir != 'u':
    #     return

    if pos in state:
        return
    
    state.add(pos)    
    frozenState = frozenset(state)
    frozenHash = hash(frozenState)
    state.remove(pos)
    del frozenState
    if frozenHash in states and states[frozenHash] >= steps:
        return

    states[frozenHash] = steps

    # if (pos, dir) in states and states[(pos, dir)] > steps:
    #     return
    
    # states[(pos, dir)] = steps

    if pos == (len(data) - 1, len(data[0]) - 2):
        if steps > answer[0]:
            print(steps)
            answer[0] = steps
        return
    

    if dir != 'd':
        state.add(pos)
        path(data, states, state, (pos[0] - 1, pos[1]), 'u', steps + 1, answer)
        state.remove(pos)
    if dir != 'u':
        state.add(pos)
        path(data, states, state, (pos[0] + 1, pos[1]), 'd', steps + 1, answer)
        state.remove(pos)
    if dir != 'r':
        state.add(pos)
        path(data, states, state, (pos[0], pos[1] - 1), 'l', steps + 1, answer)
        state.remove(pos)
    if dir != 'l':
        state.add(pos)
        path(data, states, state, (pos[0], pos[1] + 1), 'r', steps + 1, answer)
        state.remove(pos)
    

def pathHelp(data):
    states = dict()
    state = set()
    answer = [0]
    path(data, states, state, (0, 1), 'd', 0, answer)

    return answer[0]

def solution(data):
    answer = 0
    data = data.splitlines()
    answer = pathHelp(data)
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