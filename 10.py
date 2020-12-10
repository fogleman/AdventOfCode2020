import fileinput

def part1(values):
    d = [b - a for a, b in zip(values, values[1:])]
    return d.count(1) * d.count(3)

def part2(values, x, memo):
    if x == 0:
        return 1
    if x in memo:
        return memo[x]
    if x not in values:
        return 0
    memo[x] = sum(part2(values, x - i, memo)
        for i in range(1, 4))
    return memo[x]

values = list(map(int, fileinput.input()))
values.extend([0, max(values) + 3])
values.sort()

print(part1(values))
print(part2(set(values), values[-1], {}))
