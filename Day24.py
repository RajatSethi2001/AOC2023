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
        print(data[line])
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            initFirstX = data[i][0][0]
            firstXv = data[i][1][0]

            initFirstY = data[i][0][1]
            firstYv = data[i][1][1]

            initFirstXtime = -initFirstX / firstXv

            firstYoX = firstYv / firstXv
            initFirstYatX = initFirstY + firstYv * initFirstXtime 

            initSecondX = data[j][0][0]
            secondXv = data[j][1][0]

            initSecondY = data[j][0][1]
            secondYv = data[j][1][1]

            initSecondXtime = -initSecondX / secondXv

            secondYoX = secondYv / secondXv
            initSecondYatX = initSecondY + secondYv * initSecondXtime
            
            deltaYoX = -secondYoX + firstYoX
            deltaYatX = -initSecondYatX + initFirstYatX
            
            if deltaYoX == 0:
                continue

            xAnswer = -deltaYatX / deltaYoX
            yAnswer = firstYoX * xAnswer + initFirstYatX

            if (xAnswer - initFirstX) / firstXv < 0:
                continue

            if (yAnswer - initFirstY) / firstYv < 0:
                continue

            if (xAnswer - initSecondX) / secondXv < 0:
                continue

            if (yAnswer - initSecondY) / secondYv < 0:
                continue

            if xAnswer >= 200000000000000 and xAnswer <= 400000000000000:
                if yAnswer >= 200000000000000 and yAnswer <= 400000000000000:
                    answer += 1

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