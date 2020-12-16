import fileinput
import math
import re

def parse(lines):
    rules = {}
    tickets = []
    for line in lines:
        numbers = list(map(int, re.findall(r'\d+', line)))
        if '-' in line:
            rules[line.split(':')[0]] = [tuple(numbers[i:i+2])
                for i in range(0, len(numbers), 2)]
        elif numbers:
            tickets.append(numbers)
    return rules, tickets

def invalid_numbers(rules, ticket):
    return [number for number in ticket
        if not any(r[0] <= number <= r[1]
            for rule in rules.values() for r in rule)]

def rules_for_index(rules, tickets, index):
    result = []
    values = [ticket[index] for ticket in tickets]
    for name, rule in rules.items():
        if all(any(r[0] <= value <= r[1] for r in rule) for value in values):
            result.append(name)
    return result

def part1(rules, tickets):
    return sum(sum(invalid_numbers(rules, ticket))
        for ticket in tickets)

def part2(rules, tickets):
    tickets = [x for x in tickets if not invalid_numbers(rules, x)]
    index_options = [rules_for_index(rules, tickets, index)
        for index in range(len(tickets[0]))]
    done = False
    mapping = {}
    while not done:
        done = True
        for index, options in enumerate(index_options):
            if len(options) == 1:
                done = False
                name = options[0]
                mapping[name] = index
                for options in index_options:
                    if name in options:
                        options.remove(name)
    return math.prod(tickets[0][i]
        for k, i in mapping.items() if k.startswith('departure'))

rules, tickets = parse(fileinput.input())
print(part1(rules, tickets))
print(part2(rules, tickets))
