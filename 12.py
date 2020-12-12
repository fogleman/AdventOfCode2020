from math import *
import fileinput

def part1(commands):
    x = y = a = 0
    for command, value in commands:
        if command == 'N':
            y += value
        if command == 'S':
            y -= value
        if command == 'E':
            x += value
        if command == 'W':
            x -= value
        if command == 'L':
            a += value
        if command == 'R':
            a -= value
        if command == 'F':
            x += int(cos(radians(a))) * value
            y += int(sin(radians(a))) * value
    return abs(x) + abs(y)

def part2(commands):
    x = y = 0
    dx, dy = 10, 1
    for command, value in commands:
        if command == 'N':
            dy += value
        if command == 'S':
            dy -= value
        if command == 'E':
            dx += value
        if command == 'W':
            dx -= value
        if command == 'L':
            c = int(cos(radians(value)))
            s = int(sin(radians(value)))
            dx, dy = c * dx - s * dy, s * dx + c * dy
        if command == 'R':
            c = int(cos(radians(-value)))
            s = int(sin(radians(-value)))
            dx, dy = c * dx - s * dy, s * dx + c * dy
        if command == 'F':
            x += dx * value
            y += dy * value
    return abs(x) + abs(y)

commands = [(x[0], int(x[1:])) for x in fileinput.input()]
print(part1(commands))
print(part2(commands))
