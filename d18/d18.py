def run_calc(total, operation, number):
    if operation == '':
        total = number
    elif operation == '+':
        total += number
    elif operation == '*':
        total *= number
    else:
        print("FAILUE: Invalid operation")
    return total

def solve_calc(line):
    calc = 0
    op = ''
    no_calc = False
    for char in list(line):        
        if no_calc:
            if char == '(':
                nested += 1
            elif char == ')':
                nested -= 1

            if nested > 0:
                sub_set = sub_set + char
            else:
                if char == ')':
                    no_calc = False
                    calc = run_calc(calc,op,solve_calc(sub_set))
        else:
            if char.isdigit():
                calc = run_calc(calc,op,int(char))
            elif char in ['+','*']:
                op = char
            elif char == '(':
                sub_set = ''
                nested = 1
                no_calc = True
    return calc
        
#################
total = 0
for i, line in enumerate(open("input.txt"),1):
    if line:
        calc = solve_calc(line.strip().replace(' ',''))
        #print(i," = ",calc)
        total += calc
        
print("Sum Total of all values =",total)
# 30263286928615 too low
