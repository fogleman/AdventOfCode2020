import fileinput

ids = set((s := ''.join(str(int(not ord(c) & 4)) for c in x)) and
    int(s[:7], 2) * 8 + int(s[7:10], 2) for x in fileinput.input())
print(max(ids), set(range(min(ids), max(ids) + 1)) - ids)
