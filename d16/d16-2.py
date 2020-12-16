def print_results():
    print()
    print("List of rules and positions")
    for r in rules:
        print(r,"is position",rules[r]["position"])
    
def line_of_ints(line):
    return [int(s) for s in line.split(',')]

def check_ticket(line):
    good_ticket = True
    for s in line_of_ints(line):
        good_value = False
        for rule in rules:
            for r in rules[rule]["ranges"]:
                if (s >= r[0] and s <= r[1]):
                    good_value = True
                    break
        if not good_value:
            good_ticket = False
            break
    return good_ticket

def define_ticket(line):
    if check_ticket(line):
        for i, s in enumerate(line_of_ints(line)):
            for rule in rules:
                for r in rules[rule]["ranges"]:
                    if (s >= r[0] and s <= r[1]):
                        if i in rules[rule]["hits"]:
                            rules[rule]["hits"][i] += 1
                        else:
                            rules[rule]["hits"][i] = 1
        return True
    return False

def add_rule(line):
    new_rule = dict()
    rule_name = line.split(':')[0].strip()
    new_rule[rule_name] = dict()
    new_rule[rule_name]["ranges"] = list()

    for rng in line.split(':')[1].split('or'):
        start = int(rng.split('-')[0].strip())
        finish = int(rng.split('-')[1].strip())
        new_rule[rule_name]["ranges"].append([start,finish])

    new_rule[rule_name]["hits"] = dict()
    new_rule[rule_name]["position"] = -1
    return new_rule

def remove_rule_hits(rules, pos):
    for r in rules:
        if pos in rules[r]["hits"]:
            del rules[r]["hits"][pos]
    return rules

def solve_rules_order(rules):
    set_pos = 0
    while set_pos < total_positions:
        for r in rules:
            if rules[r]["position"] == -1:            
                c = -1
                for h in rules[r]["hits"]:
                    if rules[r]["hits"][h] == num_tickets:
                        if c >= 0:
                            c = -1
                            break
                        else:
                            c = h
                if c >= 0:
                    rules[r]["position"] = c
                    rules = remove_rule_hits(rules,rules[r]["position"])
                    set_pos += 1
    return
    
################
num_tickets = 0
with open("input.txt") as f:
    rules = dict()
    while True:
        x = f.readline().strip()
        if x:
            rules.update(add_rule(x))
        else:
            break

    x = f.readline()
    x = f.readline().strip()
    my_ticket = line_of_ints(x)
    if define_ticket(x):
        num_tickets += 1 

    x = f.readline().strip()
    x = f.readline().strip()
    while True:
        x = f.readline().strip()
        if x:
            if define_ticket(x):
                num_tickets += 1 
        else:
            break

total_positions = len(my_ticket)
solve_rules_order(rules)

#print_results()

depature_value = 1
for r in rules:
    if "departure" in r:
        depature_value *= my_ticket[rules[r]["position"]]
print()
print("Multiplication of depareture spots", depature_value)
print()
print("script done")
