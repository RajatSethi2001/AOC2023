from aocd import get_data, submit
from utils import *

part = 'b'
day = 9
year = 2023
example_a_answer = "114"
example_b_answer = "2"

puzzle_input = get_data(day=day, year=year)

def solution(data):
    data = data.splitlines()
    answer = 0
    for line in data:
        layers = []
        top = [int(val) for val in line.split(" ")]

        allZero = False
        currLayer = top
        while not allZero:
            allZero = True
            nextLayer = []
            for i in range(len(currLayer) - 1):
                nextVal = currLayer[i + 1] - currLayer[i]
                nextLayer.append(nextVal)

                if nextVal:
                    allZero = False
            
            layers.append(currLayer)
            currLayer = nextLayer
            print(layers)

        for l in range(len(layers) - 1, -1, -1):
            if not l:
                answer += layers[l][0]
            else:
                layers[l-1].insert(0, layers[l-1][0] - layers[l][0])

    
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