def int_list_to_str(ints):
    return [str(c) for c in ints]


def play_move(cups,current):
    if debug: print("cups  : {}".format(' '.join(int_list_to_str(cups))))
    max_cup = max(cups)
    min_cup = min(cups)
    target = cups[current]
    
    # grab next 3
    hold = list()
    for i in range(3):
        if current+1 < len(cups):
            hold.append(cups.pop(current+1))
        else:
            hold.append(cups.pop(0))

    if debug: print("pickup: {}".format(' '.join(int_list_to_str(hold))))

    # Find next spot
    nt = target
    while True:
        if nt == min_cup:
            nt = max_cup
        else:
            nt -= 1
        if debug: print("searching: {}".format(nt))
        
        if nt in cups:
            nt_pos = cups.index(nt)
            break
    
    for i,c in zip([nt_pos+1,nt_pos+2,nt_pos+3], hold):
        cups.insert(i,c)

    nc = cups.index(target)
    if nc+1 == len(cups):
        return 0, cups
    else:
        return nc+1, cups


####################################
with open("input.txt") as f:
    line = f.readline().strip()
cups = [int(i) for i in line]
debug = False
current = 0
for i in range(100):
    if debug: print("\n-- move {} --".format(i+1))
    current, cups = play_move(cups,current)

print("\n-- final --")
print("cups    : {}".format(' '.join(int_list_to_str(cups))))
print("current : {}".format(cups[current]))
