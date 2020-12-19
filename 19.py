import fileinput
import re

class Eq:
    def __init__(self, ch):
        self.ch = ch
    def resolve(self, rules):
        pass
    def match(self, xs):
        return [x[1:] for x in xs
            if len(x) > 0 and x[0] == self.ch]

class Or:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def resolve(self, rules):
        self.a.resolve(rules)
        self.b.resolve(rules)
    def match(self, xs):
        return self.a.match(xs) + self.b.match(xs)

class Seq:
    def __init__(self, items):
        self.items = items
    def resolve(self, rules):
        self.items = [rules[x] for x in self.items]
    def match(self, xs):
        rest = []
        for x in xs:
            x = [x]
            for item in self.items:
                x = item.match(x)
                if not x:
                    break
            else:
                rest.extend(x)
        return rest

def parse(s):
    s = s.strip()
    if '"' in s:
        return Eq(s[1:-1])
    if '|' in s:
        return Or(*map(parse, s.split('|')))
    return Seq(list(map(int, re.findall(r'\d+', s))))

def run(s, two):
    header, footer = [x.split('\n') for x in lines.split('\n\n')]
    rules = {}
    for line in header:
        key, rest = line.split(':')
        rules[int(key)] = parse(rest)
    if two:
        rules[8] = parse('42 | 42 8')
        rules[11] = parse('42 31 | 42 11 31')
    for rule in rules.values():
        rule.resolve(rules)
    return sum('' in rules[0].match([message]) for message in footer)

lines = ''.join(fileinput.input())
print(run(lines, False))
print(run(lines, True))
