import re

def main():
    with open('input.txt') as file:
        passports = [[]]
        i = 0
        for line in file.readlines():
            line = line.strip()
            if line == '':
                passports.append([])
                i += 1
            else:
                passports[i] += line.split(' ')

    # Part 1
    valid_count = 0
    for candidate in passports:
        valid = True
        for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if not any(field in string for string in candidate):
                valid = False
                break
        if valid:
            valid_count += 1

    print('Part 1:', valid_count)

    # Part 2
    passports_dict = []
    for p in passports:
        passports_dict.append(dict((field.split(':')) for field in p))

    valid_count = 0
    for p in passports_dict:
        if (all(field in p.keys() for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) and
           1920 <= int(p['byr']) <= 2002 and
           2010 <= int(p['iyr']) <= 2020 and
           2020 <= int(p['eyr']) <= 2030 and
           re.fullmatch('(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in', p['hgt']) and
           re.fullmatch('#[0-9a-f]{6}', p['hcl']) and
           p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and
           re.fullmatch('[0-9]{9}', p['pid'])):
            valid_count += 1

    print('Part 2:', valid_count)


if __name__ == '__main__':
    main()
