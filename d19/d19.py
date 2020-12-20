def parse_rule(line):
    key = int(line.split(':')[0])

    values = list()
    for i in line.split(':')[1].split('|'):    
        if '"' in i:
            values = i.replace('"','').strip()
        else:
            values.append([int(x) for x in i.split()])
    
    return {key : values}

def is_valid(expr, valid):
    if len(valid) > len(expr):
        return False
    elif len(valid) == 0 or len(expr) == 0:
        if len(valid) == 0 and len(expr) == 0:
            return True
        else:
            return False

    c = valid.pop()
    if c in ['a','b']:
        if expr[0] == c:
            return is_valid(expr[1:], valid.copy())
    else:
        for rule in rules[c]:
            if is_valid(expr, valid + list(reversed(rule))):
                return True
    return False

###########################
total = 0
rules = dict()
load_rules = True
for line in open("input.txt"):
    line = line.strip()
    if not line:
        load_rules = False
        # part 2 only
        #rules[8] = [[42], [42, 8]]
        #rules[11] = [[42, 31], [42, 11, 31]]
        continue
    
    if load_rules:
        rules.update(parse_rule(line))
    else:
        if is_valid(line, list(reversed(rules[0][0]))):
            total += 1

print("Total valid messages",total)
