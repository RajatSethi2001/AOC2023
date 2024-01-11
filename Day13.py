from aocd import get_data, submit
from utils import *

part = 'b'
day = 13
year = 2023
example_a_answer = "405"
example_b_answer = "400"

puzzle_input = get_data(day=day, year=year)

def fixSmudge(mirror):
    diff = None
    index = 0
    while index < len(mirror):
        refLen = min(index, len(mirror) - index)
        mirror1 = mirror[index - refLen:index]
        mirror2 = mirror[index:index + refLen][::-1]

        succ = True
        if diff is None:
            for row in range(len(mirror1)):
                for col in range(len(mirror1[row])):
                    if mirror1[row][col] != mirror2[row][col]:
                        if diff is None:
                            diff = (row, col)
                        else:
                            succ = False
                            diff = None
                            break
                if not succ:
                    break
        
        if diff is not None:
            return index * 100
        index += 1

    if diff is None:
        tMirror = list(zip(*mirror))
        tMirror = ["".join(row) for row in tMirror]
        index = 0
        while index < len(tMirror):
            refLen = min(index, len(tMirror) - index)
            mirror1 = tMirror[index - refLen:index]
            mirror2 = tMirror[index:index + refLen][::-1]

            succ = True
            if diff is None:
                for row in range(len(mirror1)):
                    for col in range(len(mirror1[row])):
                        if mirror1[row][col] != mirror2[row][col]:
                            if diff is None:
                                diff = (col, row)
                            else:
                                succ = False
                                diff = None
                                break
                    if not succ:
                        break
            
            if diff is not None:
                return index
            index += 1
    
    return 0
    # if diff is not None:
    #     row = diff[0]
    #     col = diff[1]
    #     print(diff)
    #     toChange = None
    #     if mirror[row][col] == ".":
    #         toChange = "#"
    #     else:
    #         toChange = "."
        
    #     mirror[row] = mirror[row][:col] + toChange + mirror[row][col + 1:]

# def horizontal(mirror):
#     index = 1
#     cols = 0
#     print(mirror)
#     while index < len(mirror):
#         refLen = min(index, len(mirror) - index)
        
#         if mirror[index - refLen:index] == mirror[index:index + refLen][::-1]:
#             # cols += index
#             print(index)
#             return index
        
#         index += 1
    
#     return cols

# def vertical(mirror):
#     tMirror = list(zip(*mirror))
#     tMirror = ["".join(row) for row in tMirror][::-1]
#     return horizontal(tMirror)

def solution(data):
    answer = 0
    data = data.split("\n\n")

    for mirror in data:
        mirrorList = mirror.splitlines()
        answer += fixSmudge(mirrorList)
        # answer += horizontal(mirrorList) * 100
        # answer += vertical(mirrorList)
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