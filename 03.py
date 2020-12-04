import fileinput
import math

def hits(grid, dx, dy):
    w = len(grid[0])
    h = len(grid)
    x = y = count = 0
    while y < h:
        if grid[y][x%w] == '#':
            count += 1
        x += dx
        y += dy
    return count

grid = [x.strip() for x in fileinput.input()]

# part 1
print(hits(grid, 3, 1))

# part 2
dirs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
counts = [hits(grid, dx, dy) for dx, dy in dirs]
print(math.prod(counts))
