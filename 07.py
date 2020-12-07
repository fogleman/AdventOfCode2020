import fileinput
import re

def can_contain(rules, color, target):
    return any(c == target or can_contain(rules, c, target)
        for c in rules[color])

def bag_count(rules, color):
    return sum(n + n * bag_count(rules, c)
        for c, n in rules[color].items())

rules = {}
for line in fileinput.input():
    line = line[:-2].replace(' bags', '').replace(' bag', '')
    color, rest = line.split(' contain ')
    rules[color] = {c: int(n)
        for n, c in re.findall(r'(\d+) ([^,]+)', rest)}

t = 'shiny gold'
print(sum(can_contain(rules, c, t) for c in rules))
print(bag_count(rules, t))
