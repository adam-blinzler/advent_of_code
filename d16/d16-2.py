class rule_set:
    def __init__(self, rule_name):
        self.name = rule_name
        self.ranges = list()
        self.hits = dict()
        self.position = -1

    def add_range(self, line):
        for rng in line.split(':')[1].split('or'):
            start = int(rng.split('-')[0].strip())
            finish = int(rng.split('-')[1].strip())
            self.ranges.append([start,finish])
        return
    def add_hits(self,hit_list):
        for i, s in enumerate(hit_list):
            for r in self.ranges:
                if (s >= r[0] and s <= r[1]):
                    if i in self.hits:
                        self.hits[i] += 1
                    else:
                        self.hits[i] = 1
        return
    
    def find_position(self,num_tickets):
        c = -1
        if self.position < 0:
            for h, num_hits in self.hits.items():
                if num_hits == num_tickets:
                    if c >= 0:
                        c = -1
                        break
                    else:
                        c = h
            if c >= 0:
                self.position = c
                self.hits = dict()
        return c
    
    def remove_hit_set(self, pos):
        if pos in self.hits:
            del self.hits[pos]
        return

    def print_rule_set(self):
        print("Rule: ",self.name)
        print("   Ranges   = ",self.ranges)
        print("   Hits     = ",self.hits)
        print("   Position = ", self.position)
        return
    
#################################
def print_results():
    print("\nList of rules and positions")
    for _,rs in sorted(rules.items()):
        print(rs.name.rjust(20),"is position",rs.position)
    
def line_of_ints(line):
    return [int(s) for s in line.split(',')]

def check_ticket(line):
    good_ticket = True
    for s in line_of_ints(line):
        good_value = False
        for _ , rs in rules.items():
            for r in rs.ranges:
                if (s >= r[0] and s <= r[1]):
                    good_value = True
                    break
        if not good_value:
            good_ticket = False
            break
    return good_ticket

def define_ticket(line):
    if check_ticket(line):
        for _, rs in rules.items():
            rs.add_hits(line_of_ints(line)) 
        return True
    return False

def add_rule(line):
    new_rule = dict()
    rule_name = line.split(':')[0].strip()
    new_rule[rule_name] = rule_set(rule_name)
    new_rule[rule_name].add_range(line)

    return new_rule

def remove_rule_hits(pos):
    for _, rs in rules.items():
        rs.remove_hit_set(pos)
    return

def solve_rules_order(rules):
    set_pos = 0
    while set_pos < total_positions:
        for _, rs in rules.items():
            if rs.find_position(num_tickets) >= 0:
                remove_rule_hits(rs.position)
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

print_results()

depature_value = 1
for _, rs in rules.items():
    if "departure" in rs.name:
        depature_value *= my_ticket[rs.position]

print("\nMultiplication of depareture spots", depature_value)
print("\nscript done")
