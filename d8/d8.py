def action(op):
    op_code = op.split()[0].strip()

    if op_code =='nop':
        return 0, 1
    elif op_code == 'acc':
        return int(op.split()[1].strip()), 1
    elif op_code == 'jmp':
        return 0, int(op.split()[1].strip())
    else:
        print("read error")


def attempt_program(lines):
    visit = [0]*len(lines)
    current_line = 0
    prev_line = 0
    accum = 0
    while True:
        if current_line >= len(lines):
            print("")
            print("programe finished")
            print("    last accummulator value = ", accum)
            return False
        elif visit[current_line]:
            print("programe failed with infinite loop")
            print("    last accummulator value = ", accum)
            return visit

        acc_add, mv_line = action(lines[current_line])
        visit[current_line] = 1
        accum += acc_add
        prev_line = current_line
        current_line += mv_line
        
###################33
with open("input.txt") as fl:
    lines = fl.readlines()

while not lines[-1].strip():
    lines.pop()

sus = attempt_program(lines)
if sus:
    for i, v in enumerate(sus):
        if not v:
            continue
        
        if "jmp" in lines[i]:
            old_line = lines[i]
            lines[i] = lines[i].replace("jmp","nop")
        elif "nop" in lines[i]:
            old_line = lines[i]
            lines[i] = lines[i].replace("nop","jmp")
        else:
            continue

        if attempt_program(lines):
            lines[i] = old_line
        else:
            break

print("script done")
