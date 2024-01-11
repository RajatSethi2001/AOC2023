from aocd import get_data, submit
from utils import *

part = 'b'
day = 5
year = 2023
example_a_answer = "35"
example_b_answer = "46"

puzzle_input = get_data(day=day, year=year)

INT_MAX = 1000000000000000000

class rangeNode:
    def __init__(self, start, end, child):
        self.start = start
        self.end = end
        self.child = child

def solution(data):
    maps = data.split("\n\n")
    seeds = maps[0].split(": ")[1].split(" ")
    seeds = [(int(seeds[seedIndex]), int(seeds[seedIndex]) + int(seeds[seedIndex + 1])) for seedIndex in range(0, len(seeds), 2)]
    print(seeds)

    mapQueue = []
    for map in maps[1::]:
        map = map.split("\n")[1::]
        mapDatas = []
        for line in map:
            mapData = line.split(" ")
            mapData = [int(num) for num in mapData]
            mapDatas.append(mapData)
        mapQueue.append(mapDatas)

    nextSource = []
    bin_size = 100000
    max_bin = seeds[0][1] * 100
    bin_start = 0

    while bin_start < max_bin:
        dest_node = rangeNode(bin_start, bin_start + bin_size - 1, None)
        source_node = rangeNode(bin_start, bin_start + bin_size - 1, dest_node)
        nextSource.append(source_node)

        bin_start += bin_size

    for map in mapQueue[::-1]:
        min_dest = None
        max_dest = None
        destRanges = []
        for line in map:
            range_min = line[0]
            range_max = line[0] + line[2] - 1
            source_start = line[1]
            source_end = line[1] + line[2] - 1
            destRanges.append((range_min, range_max, source_start, source_end))

            if min_dest is None or range_min < min_dest:
                min_dest = range_min
            
            if max_dest is None or range_max > max_dest:
                max_dest = range_max
        
        # print(destRanges)
        if min_dest - 1 >= 0:
            destRanges.append((0, min_dest - 1, 0, min_dest - 1))
        destRanges.append((max_dest + 1, INT_MAX, max_dest + 1, INT_MAX))

        priorSource = []
        if not len(nextSource):
            for destRange in destRanges:
                dest_node = rangeNode(destRange[0], destRange[1], None)
                source_node = rangeNode(destRange[2], destRange[3], dest_node)
                priorSource.append(source_node)

        else:
            for destRange in destRanges: 
                dest_start = destRange[0]
                dest_end = destRange[1]
                source_start = destRange[2]
                source_end = destRange[3]
                delta_prior = destRange[0] - destRange[2]

                for node in nextSource:
                    if dest_start >= node.start and dest_end <= node.end:
                        dest_node = rangeNode(dest_start, dest_end, node)
                        priorSource.append(rangeNode(dest_start - delta_prior, dest_end - delta_prior, dest_node))
                    elif dest_start <= node.start and dest_end >= node.end:
                        dest_node = rangeNode(node.start, node.end, node)
                        priorSource.append(rangeNode(node.start - delta_prior, node.end - delta_prior, dest_node))
                    elif dest_start >= node.start and dest_start <= node.end and dest_end > node.end:
                        dest_node = rangeNode(dest_start, node.end, node)
                        priorSource.append(rangeNode(dest_start - delta_prior, node.end - delta_prior, dest_node))
                    elif dest_start < node.start and dest_end <= node.end and dest_end >= node.start:
                        dest_node = rangeNode(node.start, dest_end, node)
                        priorSource.append(rangeNode(node.start - delta_prior, dest_end - delta_prior, dest_node))
        
        nextSource = priorSource
    
    trueMap = {}
    for source in nextSource:
        start = (source.start, source.end)
        while source.child is not None:
            source = source.child
        end = (source.start, source.end)
        if end in trueMap:
            trueMap[end].append(start)
        else:
            trueMap[end] = [start,]
    
    trueList = list(trueMap.items())
    trueList = sorted(trueList, key = lambda x:x[0][0])
    print(trueList)

    answer = INT_MAX
    for bin in trueList:
        success = False
        for start_range in bin[1]:
            start = start_range[0]
            end = start_range[1]
            for seed_range in seeds:
                seed_start = seed_range[0]
                seed_end = seed_range[1]

                intersect_start = max(start, seed_start)
                intersect_end = min(end, seed_end)

                if intersect_start <= intersect_end:
                    success = True
                    for seed in range(intersect_start, intersect_end + 1):
                        value = seed
                        for map in mapQueue:
                            for line in map:
                                source = line[1]
                                delta = line[2]

                                if value >= source and value < source + delta:
                                    value = (value - source) + line[0]
                                    break
                        
                        if value < answer:
                            answer = value
                
        if success == True:
            return str(answer)

    # answer = 10000000000000000000000000
    # for seed in seeds:
    #     value = seed
    #     for map in mapQueue:
    #         # print(value, end=" ")
    #         for line in map:
    #             source = line[1]
    #             delta = line[2]

    #             if value >= source and value < source + delta:
    #                 value = (value - source) + line[0]
    #                 break
    #     # print()
    #     if value < answer:
    #         answer = value

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