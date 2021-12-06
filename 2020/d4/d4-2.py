import string

def valid_info(info):
    required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for r in required:
        if not r in info:
            return False
        elif r == 'byr':
            if not len(info['byr']) == 4:
                return False
            elif not (int(info['byr']) >= 1920 and int(info['byr']) <= 2002):
                return False
        elif r == 'iyr':
            if not len(info['iyr']) == 4:
                return False
            elif not (int(info['iyr']) >= 2010 and int(info['iyr']) <= 2020):
                return False
        elif r == 'eyr':
            if not len(info['eyr']) == 4:
                return False
            elif not (int(info['eyr']) >= 2020 and int(info['eyr']) <= 2030):
                return False
        elif r == 'hgt':
            if 'cm' in info['hgt']:
                if not (int(info['hgt'].split('cm')[0]) >= 150 and int(info['hgt'].split('cm')[0]) <= 193):
                    return False
            elif 'in' in info['hgt']:
                if not (int(info['hgt'].split('in')[0]) >= 59 and int(info['hgt'].split('in')[0]) <= 76):
                    return False
            else:
                return False
        elif r == 'hcl':
            if not '#' in info['hcl']:
                return False
            elif not all(c in string.hexdigits for c in info['hcl'][1:]):
                return False
        elif r == 'ecl':
            if not info['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
                return False
        elif r == 'pid':
            if not len(info['pid']) == 9:
                return False
            elif not info['pid'].isdigit():
                return False
    return True

def build_info(lines):
    return dict((inf.split(':')[0], inf.split(':')[1])
                for line in lines
                for inf in line.split(' '))

############################################3
count = 0

with open( "input.txt" ) as fl:
    while True:
        reading = False
        lines = list()
        while True:
            line = fl.readline().strip()
            if not line:
                break
            lines.append(line)
            reading = True
        if not reading:
            break
        info = build_info(lines)
        if valid_info(info):
           count = count + 1

print(count)
print("script done")
        
