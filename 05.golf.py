import fileinput

ids = set(int(''.join(str(int(not ord(c) & 4)) for c in x[:10]), 2)
    for x in fileinput.input())
print(max(ids), set(range(min(ids), max(ids) + 1)) - ids)
