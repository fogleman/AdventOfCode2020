import fileinput
import re

records = []
for line in fileinput.input():
    m = re.match(r'(\d+)\-(\d+) (\w)\: (\w+)', line)
    a, b, letter, password = m.groups()
    records.append((int(a), int(b), letter, password))

print(sum(a <= password.count(letter) <= b
    for a, b, letter, password in records))

print(sum(((password[a-1] == letter) + (password[b-1] == letter)) == 1
    for a, b, letter, password in records))
