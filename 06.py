import fileinput

groups = [list(map(set, x.split()))
    for x in ''.join(fileinput.input()).split('\n\n')]

for f in [set.union, set.intersection]:
    print(sum(len(f(*g)) for g in groups))
