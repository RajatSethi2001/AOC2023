from aocd import get_data, submit
from utils import *
import sys
sys.setrecursionlimit(100000)

part = 'b'
day = 16
year = 2023
example_a_answer = "46"
example_b_answer = "51"

puzzle_input = get_data(day=day, year=year)

tiles = set()
points = set()
def beam(data, point, dir):
    if not inBounds(data, point):
        return

    if (point, dir) in tiles:
        return
    
    tiles.add((point, dir))
    points.add(point)
    pos = data[point[0]][point[1]]

    if pos == ".":
        if dir == 'l':
            beam(data, (point[0], point[1] - 1), dir)
        elif dir == 'r':
            beam(data, (point[0], point[1] + 1), dir)
        elif dir == 'u':
            beam(data, (point[0] - 1, point[1]), dir)
        elif dir == 'd':
            beam(data, (point[0] + 1, point[1]), dir)
    
    elif pos == "|":
        beam(data, (point[0] - 1, point[1]), 'u')
        beam(data, (point[0] + 1, point[1]), 'd')
    
    elif pos == "-":
        beam(data, (point[0], point[1] - 1), 'l')
        beam(data, (point[0], point[1] + 1), 'r')
    
    elif pos == "/":
        if dir == 'l':
            beam(data, (point[0] + 1, point[1]), 'd')
        elif dir == 'r':
            beam(data, (point[0] - 1, point[1]), 'u')
        elif dir == 'u':
            beam(data, (point[0], point[1] + 1), 'r')
        elif dir == 'd':
            beam(data, (point[0], point[1] - 1), 'l')
    
    elif pos == "\\":
        if dir == 'l':
            beam(data, (point[0] - 1, point[1]), 'u')
        elif dir == 'r':
            beam(data, (point[0] + 1, point[1]), 'd')
        elif dir == 'u':
            beam(data, (point[0], point[1] - 1), 'l')
        elif dir == 'd':
            beam(data, (point[0], point[1] + 1), 'r')
        
def solution(data):
    global tiles
    global points
    data = data.splitlines()
    answer = None

    max = 0
    for r in range(len(data)):
        tiles = set()
        points = set()
        beam(data, (r, 0), "r")
        if len(points) > max:
            max = len(points)
    
    for r in range(len(data)):
        tiles = set()
        points = set()
        beam(data, (r, len(data[r]) - 1), "l")
        if len(points) > max:
            max = len(points)

    for c in range(len(data[0])):
        tiles = set()
        points = set()
        beam(data, (0, c), "d")
        if len(points) > max:
            max = len(points)

    for c in range(len(data[0])):
        tiles = set()
        points = set()
        beam(data, (len(data) - 1, c), "u")
        if len(points) > max:
            max = len(points)
    
    answer = max
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