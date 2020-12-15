import fileinput

def run(numbers, iterations):
    last = {}
    for i in range(iterations):
        x = numbers[i] if i < len(numbers) else delta
        delta = i - last.get(x, i)
        last[x] = i
    return x

numbers = list(map(int, next(fileinput.input()).split(',')))
print(run(numbers, 2020))
print(run(numbers, 30000000))
