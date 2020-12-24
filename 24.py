import fileinput

DIRS = {
    'e': (1, 0), 'se': (0, 1), 'sw': (-1, 1),
    'w': (-1, 0), 'nw': (0, -1), 'ne': (1, -1),
}

def follow(line):
    q = r = 0
    while line:
        if line[0] in DIRS:
            key, line = line[0], line[1:]
        else:
            key, line = line[:2], line[2:]
        dq, dr = DIRS[key]
        q, r = q + dq, r + dr
    return (q, r)

def neighbors(p):
    return {(p[0] + dq, p[1] + dr)
        for dq, dr in DIRS.values()}

def step(cells):
    result = set()
    check = set.union(*[neighbors(p) for p in cells])
    for p in check:
        n = len(cells & neighbors(p))
        if p in cells:
            if n == 1 or n == 2:
                result.add(p)
        else:
            if n == 2:
                result.add(p)
    return result

def part1(lines):
    cells = set()
    for line in lines:
        cells ^= {follow(line.strip())}
    return cells

def part2(lines):
    cells = part1(lines)
    for i in range(100):
        cells = step(cells)
    return cells

lines = list(fileinput.input())
print(len(part1(lines)))
print(len(part2(lines)))
