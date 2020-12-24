import fileinput

class Node:
    def __init__(self, value, prev=None):
        self.value = value
        self.next = None
        if prev:
            prev.next = self

def destination(wrap, *cups):
    value = cups[0]
    while value in cups:
        value = (value - 2) % wrap + 1
    return value

values = list(map(int, ''.join(fileinput.input())))
# values = values + list(range(10, 1000001))

N = len(values)
T = [0] * (N + 1)
for i in range(N):
    j = (i + 1) % N
    T[values[i]] = values[j]

hi = max(values)
lookup = {}
first = node = Node(values[0])
lookup[node.value] = node
for value in values[1:]:
    node = Node(value, node)
    lookup[node.value] = node
node.next = first

node = first
for i in range(100):
    dest = lookup[destination(
        hi, node.value, node.next.value, node.next.next.value, node.next.next.next.value)]
    last = node.next.next.next
    tmp = dest.next
    dest.next = node.next
    node.next = last.next
    last.next = tmp    
    node = node.next

node = lookup[1].next
while node != lookup[1]:
    print(node.value, end='')
    node = node.next
print()

one = lookup[1]
print(one.next.value * one.next.next.value)
