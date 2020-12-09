import fileinput

def part1(numbers, n):
    for i in range(n, len(numbers)):
        x = numbers[i]
        w = set(numbers[i-n:i])
        if not any(x - y in w for y in w):
            return x

def part2(numbers, value):
    n = len(numbers)
    for s in range(2, n):
        for i in range(n-s):
            w = numbers[i:i+s]
            if sum(w) == value:
                return min(w) + max(w)

numbers = list(map(int, fileinput.input()))
print(part1(numbers, 25))
print(part2(numbers, part1(numbers, 25)))
