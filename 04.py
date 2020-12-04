import fileinput
import re

passports = [x.split() for x in ''.join(fileinput.input()).split('\n\n')]
passports = [dict(x.split(':') for x in passport) for passport in passports]

# part 1
required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
print(sum(set(passport) >= required for passport in passports))

# part 2
validators = {
    'byr': (r'(\d{4})$', lambda x: 1920 <= int(x) <= 2002),
    'iyr': (r'(\d{4})$', lambda x: 2010 <= int(x) <= 2020),
    'eyr': (r'(\d{4})$', lambda x: 2020 <= int(x) <= 2030),
    'hgt': (r'(\d+)(cm|in)$', lambda x, u: 150 <= int(x) <= 193 if u == 'cm' else 59 <= int(x) <= 76),
    'hcl': (r'(#[0-9a-f]{6})$', lambda x: True),
    'ecl': (r'(amb|blu|brn|gry|grn|hzl|oth)$', lambda x: True),
    'pid': (r'(\d{9})$', lambda x: True),
}

print(sum(all((m := re.match(pattern, passport.get(key, ''))) and func(*m.groups()) 
    for key, (pattern, func) in validators.items()) for passport in passports))
