from aocd import get_data, submit
from utils import *

part = 'b'
day = 15
year = 2023
example_a_answer = "1320"
example_b_answer = "145"

puzzle_input = get_data(day=day, year=year)

def hash(string):
    answer = 0
    for c in string:
        answer += ord(c)
        answer *= 17
        answer = answer % 256
    return answer

def solution(data):
    data = data.replace("\n", "").split(",")
    answer = 0
    boxes = dict()
    for b in range(256):
        boxes[b] = []
    
    for d in data:
        label = None
        lens = None

        if "=" in d:
            dSplit = d.split("=")
            label = dSplit[0]
            lens = int(dSplit[1])

            boxNum = hash(label)
            lensInfo = (label, lens)

            for i in range(len(boxes[boxNum])):
                if boxes[boxNum][i][0] == label:
                    boxes[boxNum][i] = lensInfo
                    break
            else:
                boxes[boxNum].append(lensInfo)
        else:
            label = d.split("-")[0]
            boxNum = hash(label)
            for i in range(len(boxes[boxNum])):
                if boxes[boxNum][i][0] == label:
                    boxes[boxNum].pop(i)
                    break

    for box in boxes:
        if not len(boxes[box]):
            continue
        boxAns = 0
        for i in range(len(boxes[box])):
            boxAns += (box + 1) * (i + 1) * boxes[box][i][1]
        answer += boxAns
    print(boxes)
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