def split(st): 
    return [c for c in st]

def num_all_yes(all_answers,num_p):
    set_ans = set(all_answers)
    if num_p == 1:
        all_yes = len(set_ans)
    else:
        all_yes = 0
        for c in set_ans:
            if all_answers.count(c) == num_p:
                all_yes += 1
    return all_yes

######################################3
total = 0

with open( "input.txt" ) as fl:
    while True:
        reading = False
        lines = list()
        psg = 0
        while True:
            line = fl.readline().strip()
            if not line:
                break

            psg += 1
            lines.extend(split(line))
            reading = True

        if not reading:
            break

        total = total + num_all_yes(lines,psg)

print(total)
