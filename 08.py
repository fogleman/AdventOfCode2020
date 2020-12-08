import fileinput

def run(program):
    ip = acc = 0
    seen = set()
    while ip < len(program):
        if ip in seen:
            return acc, False
        seen.add(ip)
        op, arg = program[ip]
        if op == 'acc':
            acc += int(arg)
        if op == 'jmp':
            ip += int(arg) - 1
        ip += 1
    return acc, True

def part1(program):
    return run(program)[0]

def part2(program):
    m = {'jmp': 'nop', 'nop': 'jmp'}
    for i in range(len(program)):
        op, arg = program[i]
        p = list(program)
        p[i] = (m.get(op, op), arg)
        acc, ok = run(p)
        if ok:
            return acc

program = [x.split() for x in fileinput.input()]
print(part1(program))
print(part2(program))
