import fileinput
import math

lines = list(fileinput.input())
t0 = int(lines[0])
rules = [(i, int(x)) for i, x in
    enumerate(lines[1].split(',')) if x.isdigit()]
ids = [x[1] for x in rules]

# part 1
print(math.prod(min(((x - t0 % x) % x, x) for x in ids)))

# part 2
def solve(rules, t, dt):
    prev = result = 0
    while True:
        if all(t % b == (b - a) % b for a, b in rules):
            result = result or t
            if prev:
                return result, t - prev
            prev = t
        t += dt

t, dt = 0, 1
for i in range(1, len(rules) + 1):
    t, dt = solve(rules[:i], t, dt)
print(t)
