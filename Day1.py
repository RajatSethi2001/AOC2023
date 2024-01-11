from aocd import get_data, get_examples, submit
from utils import *

part = 'b'
day = 1
year = 2023

puzzle_input = get_data(day=day, year=year)
example = get_examples(day=day, year=year)[0]
# example_data = example.input_data
example_data = open("input.txt", "r").read()

def puzzle(data):
    data = data.splitlines()
    answer = 0
    for line in data:
        digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        revdigits = [d[::-1] for d in digits]
        
        min_first = 100000
        min_second = 100000
        first = ""
        second = ""
        reversedline = line[::-1]
        
        for d in range(len(digits)):
            if line.find(digits[d]) < min_first and line.find(digits[d]) != -1:
                min_first = line.find(digits[d])
                first = f"{d}"
        
        for d in range(10):
            if line.find(f"{d}") < min_first and line.find(f"{d}") != -1:
                min_first = line.find(f"{d}")
                first = f"{d}"
        
        for d in range(len(revdigits)):
            if reversedline.find(revdigits[d]) < min_second and reversedline.find(revdigits[d]) != -1:
                min_second = reversedline.find(revdigits[d])
                second = f"{d}"
        
        for d in range(10):
            if reversedline.find(f"{d}") < min_second and reversedline.find(f"{d}") != -1:
                min_second = reversedline.find(f"{d}")
                second = f"{d}"
        
        answer += int(first + second)
    
    return str(answer)

example_answer = puzzle(example_data)
print(f"Your attempt: {example_answer}")
if part == 'a':
    print(f"Actual answer: {example.answer_a}")
    assert example_answer == example.answer_a
elif part == 'b':
    print(f"Actual answer: {example.answer_b}")
    assert example_answer == example.answer_b
else:
    raise Exception(f"Part {part} does not exist")

submit(puzzle(puzzle_input), part=part, day=day, year=year)