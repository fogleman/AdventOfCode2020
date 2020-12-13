import fileinput
import math

lines = list(fileinput.input())
t0 = int(lines[0])
rules = [(i, int(x)) for i, x in
    enumerate(lines[1].split(',')) if x.isdigit()]

# part 1
print(math.prod(min((x - t0 % x, x)
    for x in [rule[1] for rule in rules])))

# part 2
t, dt = 0, 1
for i in range(1, len(rules) + 1):
    u = 0
    while True:
        if all((t + a) % b == 0 for a, b in rules[:i]):
            if u:
                t, dt = u, t - u
                break
            u = t
        t += dt
print(t)
