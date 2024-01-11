from aocd import get_data, submit
from utils import *
import copy
import math

part = 'b'
day = 20
year = 2023
example_a_answer = "32000000"
example_b_answer = ""

puzzle_input = get_data(day=day, year=year)

def needCycles(cycles):
    for cycle in cycles.values():
        if cycle[1] is None:
            return True
    return False

def solution(data):
    answer = None
    data = data.splitlines()
    pulses = dict()

    for line in data:
        lSplit = line.split(" -> ")
        if lSplit[0][0] == '&':
            # Pulse, Type, Connections, Extra
            pulses[lSplit[0][1:]] = ["C", dict(), lSplit[1].split(", ")]
        elif lSplit[0][0] == '%':
            pulses[lSplit[0][1:]] = ["F", False, lSplit[1].split(", ")]
        else:
            pulses[lSplit[0]] = ["O", False, lSplit[1].split(", ")]

    outputs = [] 
    for name, button in pulses.items():
        for output in button[-1]:
            if output not in pulses:
                outputs.append(output)

            elif pulses[output][0] == 'C':
                pulses[output][1][name] = False
    
    for output in outputs:
        pulses[output] = ["O", False, []]

    inputs = dict()
    for name, button in pulses.items():
        outputs = button[-1]
        for o in outputs:
            if o in inputs:
                inputs[o].append(name)
            else:
                inputs[o] = [name]
    print(inputs)
    revStates = ['rx']
    highest = []
    while len(revStates):
        state = revStates.pop(0)
        high = False
        for parent in inputs[state]:
            if pulses[parent][0] != 'C':
                high = True
                break
        if high:
            highest.append(state)
        else:
            revStates += inputs[state]
    
    print(highest)
    # iters = 1000
    stateList = []
    pushes = 0
    lows = 0
    highs = 0
    # initState = dict()

    cycles = dict()
    # for state in highest:
    #     cycles[highest] = [None, None]
    for key in pulses['zh'][1]:
        cycles[key] = [None, None]


    # while (initState != pulses or pushes == 1) and pushes < iters:
    while needCycles(cycles):
        pressQ = [('broadcaster', 'button', False)]
        lows += 1
        pushes += 1
        while len(pressQ):
            press = pressQ.pop(0)
            state = press[0]
            parent = press[1]
            high = press[2]
            stateData = pulses[state]

            if parent in cycles and cycles[parent][1] is None and high:
                if cycles[parent][0] is None:
                    cycles[parent][0] = pushes
                else:
                    cycles[parent][1] = pushes
            # if state == 'rx' and not high:
            #     return str(pushes)
            # print(f"Button {state} got pulse {high} from {parent}\nPulses: {pulses}")
            if stateData[0] == "F":
                if not high:
                    stateData[1] = not stateData[1]
                    for button in stateData[2]:
                        pressQ.append((button, state, stateData[1]))
                        if stateData[1]:
                            highs += 1
                        else:
                            lows += 1
            
            elif stateData[0] == "C":
                stateData[1][parent] = high
                allHigh = True
                for input in stateData[1]:
                    if stateData[1][input] == False:
                        allHigh = False
                        break
                
                for button in stateData[2]:
                    pressQ.append((button, state, not allHigh))
        
                    if not allHigh:
                        highs += 1
                    else:
                        lows += 1
                
            else:
                for button in stateData[2]:
                    pressQ.append((button, state, False))
                    lows += 1
            
        print(pushes)
        if pushes == 1:
            initLows = lows
            initHighs = highs
            lows = 0
            highs = 0
            initState = copy.deepcopy(pulses)
        else:
            stateList.append((lows, highs))
    
    print(cycles)
    
    # print(stateList)
    # cycleLen = len(stateList)
    # repeats = (iters - 1) // cycleLen
    # remain = (iters - 1) % cycleLen
    
    # ansLows = initLows + lows * repeats 
    # ansHighs = initHighs + highs * repeats

    # print(initLows, initHighs)
    # print(ansLows, ansHighs)
    # if remain > 0:
    #     ansLows += stateList[remain - 1][0]
    #     ansHighs += stateList[remain - 1][1]
    
    # print(ansLows, ansHighs)
    # answer = ansLows * ansHighs
    return str(answer)

if part == 'a':
    example_data = open("examplea.txt", "r").read()
    your_answer = solution(example_data)
    print(f"Your attempt: {your_answer}")
    print(f"Actual answer: {example_a_answer}")
    assert your_answer == example_a_answer

# elif part == 'b':
#     example_data = open("exampleb.txt", "r").read()
#     your_answer = solution(example_data)
#     print(f"Your attempt: {your_answer}")
#     print(f"Actual answer: {example_b_answer}")
#     # assert your_answer == example_b_answer

solution(puzzle_input)
# submit(solution(puzzle_input), part=part, day=day, year=year)