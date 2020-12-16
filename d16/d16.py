def check_ticket(line):
    bad_values = list()
    for s in [int(s) for s in line.split(',')]:
        good_value = False
        for r in rules:
            if (s >= r[0] and s <= r[1]):
                good_value = True
                break
        if not good_value:
          bad_values.append(s)
    return bad_values

def get_rule(line):
    return [[int(r.strip().split('-')[0]),int(r.strip().split('-')[1])] for r in line.split(':')[1].split('or')]    

################
bad_v = list()
with open("input.txt") as f:
    rules = list()
    while True:
        x = f.readline().strip()
        if x:
            if "your ticket" in x:
                break
            rules.extend(get_rule(x))
    while True:
        x = f.readline().strip()
        if x:
            if "nearby tickets" in x:
                break
            bad_v.extend(check_ticket(x))

    while True:
        x = f.readline().strip()
        if x:
            bad_v.extend(check_ticket(x))
        else:
            break

print("Ticket scanning error rate = ",sum(bad_v))
print("script done")
