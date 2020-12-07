def valid_info(info):
    required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for r in required:
        if not r in info:
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
