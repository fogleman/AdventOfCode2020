import fileinput

def scan(grid, x, y, w, h, dx, dy, one):
    nx = x + dx
    ny = y + dy
    while nx >= 0 and ny >= 0 and nx < w and ny < h:
        if grid[ny][nx] == '#':
            return 1
        if grid[ny][nx] == 'L':
            return 0
        if one:
            break
        nx += dx
        ny += dy
    return 0

def step(grid, one):
    result = [list(row) for row in grid]
    w = len(grid[0])
    h = len(grid)
    limit = 4 if one else 5
    changed = False
    for y in range(h):
        for x in range(w):
            n = sum(scan(grid, x, y, w, h, dx, dy, one)
                for dy in [-1, 0, 1] for dx in [-1, 0, 1] if dx or dy)
            if grid[y][x] == 'L' and n == 0:
                result[y][x] = '#'
                changed = True
            if grid[y][x] == '#' and n >= limit:
                result[y][x] = 'L'
                changed = True
    return result, changed

def run(grid, one):
    grid = [list(row) for row in grid]
    while True:
        grid, changed = step(grid, one)
        if not changed:
            return sum(x == '#' for row in grid for x in row)

grid = [list(line.strip()) for line in fileinput.input()]
print(run(grid, True))
print(run(grid, False))
