import copy

#################
def solve_calc(it):
    items = copy.deepcopy(it)
    while True:
        if '+' in items:
            c = items.index('+')
            items[c-1] = str(int(items[c-1]) + int(items[c+1]))
            del items[c+1]
            del items[c]
        else:
            break
    
    calc = eval(''.join(items))
    return calc

def parse_calc(it):
    items = copy.deepcopy(it)
    nested = 0
    sub_set = list()
    
    while len(items) > 1:
        for i, char in enumerate(items): 
            if nested == 0:
                if char == '(':
                    n_start = i
                    nested = 1
                    sub_set = list()
                else:
                    sub_set.append(char)
            else:
                if char == '(':
                    nested += 1
                elif char == ')':
                    nested -= 1

                if nested > 0:
                    sub_set.append(char)

                else:
                    items[n_start] = str(parse_calc(sub_set))
                    del items[n_start+1:n_start+len(sub_set)+2]
                    sub_set = list()
                    break

        if len(sub_set) >= 3:
            items[0] = str(solve_calc(sub_set))
            del items[1:len(sub_set)]
            sub_set = list()

    return int(items[0])
        
#################
total = 0
for i, line in enumerate(open("input.txt"),1):
    if line:
        calc = parse_calc(list(line.strip().replace(' ','')))
#        print(i," = ",calc)
        total += calc
        
print("Sum Total of all values =",total)
