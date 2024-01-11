from aocd import get_data, submit
from utils import *

part = 'b'
day = 14
year = 2023
example_a_answer = "136"
example_b_answer = "64"

puzzle_input = get_data(day=day, year=year)

def north(data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "O":
                for newRow in range(row - 1, -2, -1):
                    if newRow == -1 or data[newRow][col] != ".":
                        data[row] = data[row][:col] + '.' + data[row][col + 1:]
                        data[newRow + 1] = data[newRow + 1][:col] + 'O' + data[newRow + 1][col + 1:]
                        break

def south(data):
    for row in range(len(data) - 1, -1, -1):
        for col in range(len(data[row])):
            if data[row][col] == "O":
                for newRow in range(row + 1, len(data) + 1):
                    if newRow == len(data) or data[newRow][col] != ".":
                        data[row] = data[row][:col] + '.' + data[row][col + 1:]
                        data[newRow - 1] = data[newRow - 1][:col] + 'O' + data[newRow - 1][col + 1:]
                        break

def east(data):
    for row in range(len(data)):
        for col in range(len(data[row]) - 1, -1, -1):
            if data[row][col] == "O":
                for newCol in range(col + 1, len(data[row]) + 1):
                    if newCol == len(data[row]) or data[row][newCol] != ".":
                        data[row] = data[row][:col] + '.' + data[row][col + 1:]
                        data[row] = data[row][:newCol - 1] + 'O' + data[row][newCol:]
                        break

def west(data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "O":
                for newCol in range(col - 1, -2, -1):
                    if newCol == -1 or data[row][newCol] != ".":
                        data[row] = data[row][:col] + '.' + data[row][col + 1:]
                        data[row] = data[row][:newCol + 1] + 'O' + data[row][newCol + 2:]
                        break

def solution(data):
    answer = 0
    data = data.splitlines()

    states = dict()
    index = 0

    state = tuple(data)
    # states[state] = index
    while state not in states or index == 0:
        states[state] = index
        north(data)
        
        west(data)
        
        south(data)
        
        east(data)
            
        index += 1

        state = tuple(data)
        if index <= 3:
            print(state, index)
        
        
    cycleStart = states[state]
    cycleLen = index - cycleStart
    cycleRem = (1000000000 - cycleStart) % cycleLen

    for _ in range(cycleRem):
        north(data)
        
        west(data)
        
        south(data)
        
        east(data)

    answer = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 'O':
                answer += len(data) - row
    
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