import fileinput
import re

def score(deck):
    return sum(v * (len(deck) - i)
        for i, v in enumerate(deck))

def play(p1, p2):
    p1 = list(p1)
    p2 = list(p2)
    while p1 and p2:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return p1, p2

def play_recursive(p1, p2):
    p1 = list(p1)
    p2 = list(p2)
    memo = set()
    while p1 and p2:
        key = (tuple(p1), tuple(p2))
        if key in memo:
            return 1, p1, p2
        memo.add(key)
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
            winner = play_recursive(p1[:c1], p2[:c2])[0]
        else:
            winner = 1 if c1 > c2 else 2
        if winner == 1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return winner, p1, p2

def part1(p1, p2):
    p1, p2 = play(p1, p2)
    print(max(score(p1), score(p2)))

def part2(p1, p2):
    _, p1, p2 = play_recursive(p1, p2)
    print(max(score(p1), score(p2)))

numbers = list(map(int, re.findall(r'\d+',
    ''.join(fileinput.input()))))
p1 = numbers[:len(numbers)//2][1:]
p2 = numbers[len(numbers)//2:][1:]
part1(p1, p2)
part2(p1, p2)
