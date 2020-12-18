from itertools import *
import fileinput

def step(cells, dim):
    result = set()
    bounds = lambda cells, i: range(
        min(p[i] for p in cells) - 1,
        max(p[i] for p in cells) + 2)
    ranges = [bounds(cells, i) for i in range(dim)]
    for p in product(*ranges):
        n = 0
        for d in product([-1, 0, 1], repeat=dim):
            q = tuple(pp + dd for pp, dd in zip(p, d))
            n += q != p and q in cells
        if p in cells:
            if n == 2 or n == 3:
                result.add(p)
        else:
            if n == 3:
                result.add(p)
    return result

def run(cells, dim):
    pad = (0,) * (dim - 2)
    cells = set(p + pad for p in cells)
    for i in range(6):
        cells = step(cells, dim)
    return len(cells)

cells = set((x, y)
    for y, line in enumerate(fileinput.input())
        for x, c in enumerate(line) if c == '#')

print(run(cells, 3))
print(run(cells, 4))
