import fileinput

def partition(s, n, c):
    lo, hi = 0, n - 1
    for x in s:
        mid = (lo + hi) // 2
        if x == c:
            hi = mid
        else:
            lo = mid + 1
    return lo

def decode(s):
    row = partition(s[:7], 128, 'F')
    col = partition(s[7:10], 8, 'L')
    return row * 8 + col

ids = list(sorted(decode(s)
    for s in fileinput.input()))

# part 1
print(ids[-1])

# part 2
for a, b in zip(ids, ids[1:]):
    if b - a == 2:
        print(b - 1)
