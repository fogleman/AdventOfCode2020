import fileinput

ids = set(sum(('FBLR'.index(x[9-i])&1)<<i for i in range(10))
    for x in fileinput.input())

print(max(ids), set(range(min(ids), max(ids))) - ids)
