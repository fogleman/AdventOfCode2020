import fileinput

def loops(key):
    i = 0
    x = 1
    while True:
        i += 1
        x = (x * 7) % 20201227
        if x == key:
            return i

def transform(number, iterations):
    x = 1
    for i in range(iterations):
        x = (x * number) % 20201227
    return x

keys = list(map(int, fileinput.input()))
print(transform(keys[1], loops(keys[0])))
