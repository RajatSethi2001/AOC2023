from aocd import get_data, submit
from utils import *

part = 'b'
day = 11
year = 2023
example_a_answer = "374"
example_b_answer = "8410"

puzzle_input = get_data(day=day, year=year)

def solution(data):
    data = data.splitlines()
    colGaps = []
    rowGaps = []
    col = 0
    while col < len(data[0]):
        empty = True
        for row in range(len(data)):
            if data[row][col] != ".":
                empty = False
                break
        
        if empty:
            colGaps.append(col)
        #     for row in range(len(data)):
        #         data[row] = data[row][:col] + "." + data[row][col:]
        #     col += 1
        
        col += 1
    
    row = 0
    while row < len(data):
        if len(set(data[row])) == 1:
            rowGaps.append(row)
            # data.insert(row, data[row])
            # row += 1
        
        row += 1
    
    galMap = set()
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] != ".":
                galMap.add((row, col)) 
    
    print(rowGaps, colGaps)
    answer = 0
    for val in galMap:
        for otherVal in galMap:
            maxRow = max(otherVal[0], val[0])
            maxCol = max(otherVal[1], val[1])
            minRow = min(otherVal[0], val[0])
            minCol = min(otherVal[1], val[1])
            answer += abs(otherVal[0] - val[0]) + abs(otherVal[1] - val[1])

            for rowGap in rowGaps:
                if rowGap > minRow and rowGap < maxRow:
                    answer += 999999
            
            for colGap in colGaps:
                if colGap > minCol and colGap < maxCol:
                    answer += 999999

    answer = answer // 2
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
    # assert your_answer == example_b_answer

submit(solution(puzzle_input), part=part, day=day, year=year)