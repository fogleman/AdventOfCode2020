import fileinput
import functools
import itertools
import operator

def search(values, total, count):
    for group in itertools.combinations(values, count - 1):
        need = total - sum(group)
        if need in values:
            return functools.reduce(operator.mul, group, need)

values = set(map(int, fileinput.input()))
print(search(values, 2020, 2))
print(search(values, 2020, 3))
