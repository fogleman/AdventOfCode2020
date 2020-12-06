import fileinput

groups = [x.split() for x in ''.join(fileinput.input()).split('\n\n')]

for f in [set.union, set.intersection]:
    print(sum(len(f(*map(set, g))) for g in groups))
