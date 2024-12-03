import re

with open("input.txt") as f:
    data = f.read()

pattern = re.compile(r"mul\(\d+,\d+\)")

muls = pattern.findall(data)

def eval_match(match):
    terms = match.split(",")
    return int(terms[0][4:]) * int(terms[1][:-1])

print("Part 1:", sum(map(eval_match, muls)))


pattern2 = re.compile(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))")

commands = pattern2.findall(data)

do = True
result = 0
for command in commands:
    if command == "do()":
        do = True
    elif command == "don't()":
        do = False
    else:
        if not do:
            continue
        result += eval_match(command)

print("Part 2:", result)