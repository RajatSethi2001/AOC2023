from aocd import get_data, submit
from utils import *

part = 'b'
day = 22
year = 2023
example_a_answer = "5"
example_b_answer = "7"

puzzle_input = get_data(day=day, year=year)

def intersect(b1, b2):
    b1_xRange = (b1[0][0], b1[1][0])
    b2_xRange = (b2[0][0], b2[1][0])

    b1_yRange = (b1[0][1], b1[1][1])
    b2_yRange = (b2[0][1], b2[1][1])

    return max(b1_xRange[0], b2_xRange[0]) <= min(b1_xRange[1], b2_xRange[1]) and max(b1_yRange[0], b2_yRange[0]) <= min(b1_yRange[1], b2_yRange[1])

def solution(data):
    answer = None
    bricks = []
    data = data.splitlines()
    for line in data:
        bounds = line.split("~")
        start = [int(b) for b in bounds[0].split(",")]
        end = [int(b) for b in bounds[1].split(",")]
        bricks.append([start, end])
    
    bricks.sort(key = lambda x: x[0][2])
    dropped = True
    while dropped:
        dropped = False
        print("Cycled")
        for b in range(len(bricks)):
            high = 0
            maxBz = max(bricks[b][0][2], bricks[b][1][2])
            for c in range(len(bricks)):
                if c == b:
                    continue
                
                minCz = min(bricks[c][0][2], bricks[c][1][2])
                maxCz = max(bricks[c][0][2], bricks[c][1][2])
                if minCz >= maxBz:
                    continue

                if not intersect(bricks[b], bricks[c]):
                    continue

                if maxCz > high:
                    high = maxCz
            
            
            bHeight = bricks[b][1][2] - bricks[b][0][2]
            if (bricks[b][0][2] > high + 1):
                bricks[b][0][2] = high + 1
                bricks[b][1][2] = high + 1 + bHeight
                dropped = True
    
    supports = dict()
    supported = dict()
    for b in range(len(bricks)):
        supports[str(bricks[b])] = []
        for c in range(len(bricks)):
            if c == b:
                continue

            if not intersect(bricks[b], bricks[c]):
                continue
                
            if bricks[b][1][2] + 1 == bricks[c][0][2]:
                supports[str(bricks[b])].append(bricks[c])
                if str(bricks[c]) not in supported:
                    supported[str(bricks[c])] = []
                
                supported[str(bricks[c])].append(bricks[b])
    
    answer = 0
    disint = dict()
    for b in supports:
        if len(supports[b]) == 0:
            # answer += 1
            continue
        
        safe = 0
        willFall = []
        for above in supports[b]:
            # print(supported[str(above)])
            if len(supported[str(above)]) > 1:
                safe += 1
            else:
                willFall.append(above)
        
        disint[b] = willFall
        # if safe == len(supports[b]):
        #     answer += 1

    print(disint)    
    for b in disint:
        defFall = set()
        defFall.add(str(b))
        for brick in disint[b]:
            defFall.add(str(brick))
        collectSupp = set()

        accounted = set()

        moreBricks = True
        while moreBricks:
            moreBricks = False
            for brick in defFall:
                if str(brick) in accounted:
                    continue
                accounted.add(brick)
                if str(brick) in supports:
                    for above in supports[str(brick)]:
                        collectSupp.add(str(above))
                        moreBricks = True
            
            for brick in collectSupp:
                needs = set([str(need) for need in supported[str(brick)]])
                if len(needs.difference(defFall)) == 0:
                    defFall.add(str(brick))

        answer += len(defFall) - 1
        print(len(defFall) - 1)

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