from aocd import get_data, submit
from utils import *

part = 'b'
day = 19
year = 2023
example_a_answer = "19114"
example_b_answer = "167409079868000"

puzzle_input = get_data(day=day, year=year)

def getRanges(ruleRanges, state):
    rangeList = []
    for cond in ruleRanges[state]:
        priorState = cond[0]
        distRanges = []
        if priorState in ruleRanges:
            newRanges = getRanges(ruleRanges, priorState)
            for r in newRanges:
                distRanges = r + cond[1:]
        else:
            distRanges = cond[1:]
        
        # print(distRanges)
        rangeList.append(distRanges)
    
    # print(rangeList)
    return rangeList

def solution(data):
    answer = 0
    data = data.split("\n\n")
    rules = data[0].splitlines()
    parts = data[1].splitlines()

    ruleDict = dict()
    for rule in rules:
        ruleStrip = rule.replace("}", "")
        ruleSplit = ruleStrip.split("{")
        ruleDict[ruleSplit[0]] = ruleSplit[1].split(",")
    
    ruleRanges = dict()
    for ruleState in ruleDict:
        priorConds = []
        for rule in ruleDict[ruleState]:
            ruleSplit = rule.split(":")
            if len(ruleSplit) == 2:
                nextState = ruleSplit[1]
                cond = ruleSplit[0]
            else:
                nextState = ruleSplit[0]
                cond = ""

            if '<' in cond:
                condSplit = cond.split('<')
                condVar = condSplit[0]
                condBound = int(condSplit[1])

                condRange = (1, condBound - 1)
                invRange = (condBound, 4000)
                if nextState in ruleRanges:
                    ruleRanges[nextState].append([ruleState, (condVar, condRange)] + priorConds)
                else:
                    ruleRanges[nextState] = [[ruleState, (condVar, condRange)] + priorConds]
                
                priorConds.append((condVar, invRange))
            
            elif '>' in cond:
                condSplit = cond.split('>')
                condVar = condSplit[0]
                condBound = int(condSplit[1])

                condRange = (condBound + 1, 4000)
                invRange = (1, condBound)
                if nextState in ruleRanges:
                    ruleRanges[nextState].append([ruleState, (condVar, condRange)] + priorConds)
                else:
                    ruleRanges[nextState] = [[ruleState, (condVar, condRange)] + priorConds]
                
                priorConds.append((condVar, invRange))
            
            else:
                if nextState in ruleRanges:
                    ruleRanges[nextState].append([ruleState,] + priorConds)
                else:
                    ruleRanges[nextState] = [[ruleState,] + priorConds]

    # print(ruleRanges)

    acceptRanges = getRanges(ruleRanges, 'A')
    print(acceptRanges)

    for andRanges in acceptRanges:
        inters = 1
        charRanges = dict()
        for partRange in andRanges:
            rangeChar = partRange[0]
            rangeVals = partRange[1]
            if rangeChar in charRanges:
                charRanges[rangeChar] = (max(charRanges[rangeChar][0], rangeVals[0]), min(charRanges[rangeChar][1], rangeVals[1]))
            else:
                charRanges[rangeChar] = rangeVals
        
        for charRange in charRanges.values():
            inters *= (charRange[1] - charRange[0] + 1)
        
        inters *= 4000 ** (4 - len(charRanges))
        answer += int(inters)
    # partDict = dict()
    # partDict['x'] = 0
    # partDict['m'] = 0
    # partDict['a'] = 0
    # partDict['s'] = 0
    # for part in parts:
    #     partStrip = part.replace("{","").replace("}","")
    #     partSplit = partStrip.split(",")
    #     for p in partSplit:
    #         pSplit = p.split("=")
    #         partDict[pSplit[0]] = int(pSplit[1])
        
    # state = "in"
    # accept = sum(partDict.values())
    # while state != "R" and state != "A":
    #     conds = ruleDict[state]
    #     for cond in conds:
    #         if ":" not in cond:
    #             state = cond
    #             break
    #         else:
    #             condSplit = cond.split(":")
    #             if eval(f"partDict['{condSplit[0][0]}']{condSplit[0][1:]}"):
    #                 state = condSplit[1]
    #                 break
        
        # if state == "A":
        #     answer += accept
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