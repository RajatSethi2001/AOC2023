from aocd import get_data, submit
from utils import *
from collections import Counter

part = 'b'
day = 7
year = 2023
example_a_answer = "6440"
example_b_answer = "5905"

puzzle_input = get_data(day=day, year=year)

def fiveOfAKind(hand):
    count = list(dict(Counter(hand)).items())
    return count[0][1] == 5 or (len(count) == 2 and (count[0][0] == 'J' or count[1][0] == 'J'))

def fourOfAKind(hand):
    dictCount = dict(Counter(hand))
    count = list(dict(Counter(hand)).items())

    if 'J' in dictCount:
        if dictCount['J'] >= 3:
            return True
        elif dictCount['J'] == 2:
            newHand = ""
            for card in dictCount:
                if card != 'J':
                    newHand += card * dictCount[card]
            if onePair(newHand):
                return True
        elif dictCount['J'] == 1:
            newHand = ""
            for card in dictCount:
                if card != 'J':
                    newHand += card * dictCount[card]
            if threeOfAKind(newHand):
                return True
            
    for card in count:
        if card[1] >= 4:
            return True
    return False

def fullHouse(hand):
    dictCount = dict(Counter(hand))
    count = list(dict(Counter(hand)).items())
    twoKind = False
    threeKind = False

    if 'J' in dictCount:
        if dictCount['J'] >= 3:
            return True
        elif dictCount['J'] == 2:
            newHand = ""
            for card in dictCount:
                if card != 'J':
                    newHand += card * dictCount[card]
            if onePair(newHand):
                return True
        elif dictCount['J'] == 1:
            newHand = ""
            for card in dictCount:
                if card != 'J':
                    newHand += card * dictCount[card]
            if twoPair(newHand):
                return True
            
    for card in count:
        if card[1] == 2:
            twoKind = True
        if card[1] == 3:
            threeKind = True
    
    return twoKind and threeKind

def threeOfAKind(hand):
    dictCount = dict(Counter(hand))
    count = list(dict(Counter(hand)).items())

    if 'J' in dictCount and dictCount['J'] == 2:
        return True
    
    for card in count:
        if card[1] >= 3:
            return True
        elif card[1] == 2 and 'J' in hand:
            return True
    return False

def twoPair(hand):
    dictCount = dict(Counter(hand))
    count = list(dict(Counter(hand)).items())
    onePairCard = False

    if 'J' in dictCount:
        if dictCount['J'] == 2:
            return True
        elif dictCount['J'] == 1:
            newHand = ""
            for card in dictCount:
                if card != 'J':
                    newHand += card * dictCount[card]
            if onePair(newHand):
                return True
            
    for card in count:
        if not onePairCard:
            if card[1] >= 2:
                onePairCard = True
        else:
            if card[1] >= 2:
                return True
    
    return False

def onePair(hand):
    count = list(dict(Counter(hand)).items())
    if 'J' in hand:
        return True
    
    for card in count:
        if card[1] >= 2:
            return True
    return False

def value(hand):
    if fiveOfAKind(hand):
        return 7
    
    elif fourOfAKind(hand):
        return 6
    
    elif fullHouse(hand):
        return 5
    
    elif threeOfAKind(hand):
        return 4
    
    elif twoPair(hand):
        return 3
    
    elif onePair(hand):
        return 2
    
    return 1

def compare(hand1, hand2):
    value1 = value(hand1)
    value2 = value(hand2)

    priority = ['A', 'K', 'Q', 'T']
    for i in range(9, 1, -1):
        priority.append(str(i))
    priority.append('J')
    priority = priority[::-1]

    priorityMap = {}
    for index in range(len(priority)):
        priorityMap[priority[index]] = index

    if value1 == value2:
        for c in range(len(hand1)):
            card1 = hand1[c]
            card2 = hand2[c]

            if priorityMap[card1] > priorityMap[card2]:
                return True
            elif priorityMap[card1] < priorityMap[card2]:
                return False
        return False
    
    return value1 > value2

def solution(data):
    data = data.splitlines()
    data = [line.split(" ") for line in data]

    handList = []
    for hand in data:
        index = 0
        for otherHand in handList:
            if compare(hand[0], otherHand[0]):
                index += 1
            else:
                handList.insert(index, hand)
                break
        else:
            handList.append(hand)
    
    answer = 0
    rank = 1
    for hand in handList:
        answer += rank * int(hand[1])
        rank += 1
    
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