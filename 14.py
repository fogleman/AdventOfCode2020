import fileinput
import re

def parse_mask(mask, ch):
    return sum(1 << 35-i for i, c in enumerate(mask) if c == ch)

def part1(lines):
    mem = {}
    for line in lines:
        if line.startswith('mask'):
            mask = line.split()[-1]
            mask0 = parse_mask(mask, '0')
            mask1 = parse_mask(mask, '1')
        else:
            address, value = map(int, re.findall(r'\d+', line))
            mem[address] = value & ~mask0 | mask1
    return sum(mem.values())

def part2(lines):
    mem = {}
    for line in lines:
        if line.startswith('mask'):
            mask = list(line.split()[-1])
            n = mask.count('X')
            floating = parse_mask(mask, 'X')
            indices = [i for i, x in enumerate(mask) if x == 'X']
            masks0 = []
            masks1 = []
            for k in range(1 << n):
                b = bin(k | (1 << n))[3:]
                for i, j in enumerate(indices):
                    mask[j] = b[i]
                masks0.append(parse_mask(mask, '0') & floating)
                masks1.append(parse_mask(mask, '1'))
        else:
            address, value = map(int, re.findall(r'\d+', line))
            for mask0, mask1 in zip(masks0, masks1):
                mem[address & ~mask0 | mask1] = value
    return sum(mem.values())

lines = list(fileinput.input())
print(part1(lines))
print(part2(lines))
