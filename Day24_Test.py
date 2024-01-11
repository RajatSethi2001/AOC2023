from aocd import get_data, submit
from utils import *

part = 'a'
day = 24
year = 2023
example_a_answer = ""
example_b_answer = ""

puzzle_input = get_data(day=day, year=year)

def solution(data):
    answer = 0
    data = data.splitlines()
    for line in range(len(data)):
        lineSplit = data[line].split(" @ ")
        pos = [int(p) for p in lineSplit[0].split(", ")]
        vel = [int(p) for p in lineSplit[1].split(", ")]
        data[line] = [pos, vel]
        # print(data[line])
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            constX = data[i][0][0] - data[j][0][0]
            sX = data[j][1][0]
            tX = -data[i][1][0]

            constX /= -sX
            tX /= -sX
            sX /= -sX

            constY = data[i][0][1] - data[j][0][1]
            sY = data[j][1][1]
            tY = -data[i][1][1]

            constY /= sY
            tY /= sY
            sY /= sY

            if (tX + tY) == 0:
                print(f"0 T: {data[i]}, {data[j]}")
                continue 
            t = (constX + constY) / (tX + tY)
            s = constY - (t * tY)

            if data[i][0][2] + (data[i][1][2] * t) == data[j][0][2] + (data[j][1][2] * s):
                print(data[i], data[j])

    return str(answer)

if part == 'a':
    example_data = open("examplea.txt", "r").read()
    # your_answer = solution(example_data)
    # print(f"Your attempt: {your_answer}")
    # print(f"Actual answer: {example_a_answer}")
    # assert your_answer == example_a_answer

elif part == 'b':
    example_data = open("exampleb.txt", "r").read()
    your_answer = solution(example_data)
    print(f"Your attempt: {your_answer}")
    print(f"Actual answer: {example_b_answer}")
    assert your_answer == example_b_answer

print(solution(puzzle_input))
# submit(solution(puzzle_input), part=part, day=day, year=year)