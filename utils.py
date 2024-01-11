import typing

def typeWrapper(data, type):
    for i in range(len(data)):
        data[i] = type(data[i])
    return data

def readFile(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
        return data

def inBounds(data, index):
    if not len(index):
        return True
    
    dim = index[0]
    if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, str):
        if not isinstance(dim, int) or dim < 0 or dim >= len(data):
            return False
        return inBounds(data[dim], index[1::])

    elif isinstance(data, dict):
        if not isinstance(dim, typing.Hashable) or not dim in data:
            return False
        return inBounds(data[dim], index[1::])
    
    #Index has more values, but data is not indexable.
    return False

class Node:
    def __init__(self):
        self.id = None
        self.data = {}
        self.parent = None
        self.children = []

def Dijkstra(start):
    winners = {}
    contenders = {start.id: [start, 0]}
    currentNode = start
    currentDist = 0
    
    while len(contenders) != 0:
        
        
        contenderList = list(contenders.items())
        sortedContenders = sorted(contenderList, key=lambda x: x[1][1])
        newWinner = sortedContenders[0]
        currentNode = newWinner[1][0]
        currentDist = newWinner[1][1]
        contenders.pop(newWinner[0])
        winners[newWinner[0]] = [currentNode, currentDist]

        for neighbor in currentNode.children:
            neighborNode = neighbor[0]
            neighborID = neighborNode.id
            neighborDist = neighbor[1]
            newDist = currentDist + neighborDist
            
            if neighborID not in winners:
                if neighborID not in contenders:
                    contenders[neighborID] = [neighborNode, newDist]
                else:
                    if newDist < contenders[neighborID][1]:
                        contenders[neighborID][1] = newDist
    
    return winners
