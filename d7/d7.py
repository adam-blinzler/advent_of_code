def check_inners(rule):
    if target in rules[rule]:
        return 1
    for bag in rules[rule]:
        if check_inners(bag):
            return 1
    return 0

def part1():
    count = 0
    for rule in rules:
        #print(rule)
        if rule == target:
            next
        else:
            count += check_inners(rule)      
    print('part 1 = ',count)

#########################

def counting(rule):
    count = 0
    for bag in rules[rule]:
        count += rules[rule][bag]
        count += rules[rule][bag] * counting(bag)
    return count
                              
def part2():
    print('part 2 = ',counting(target))

##############################
target = "shiny gold"
rules = dict()

for line in open("input.txt"):
    main = line.split("bags contain")[0].strip()
    rules[main] = dict()
    inside = line.split("bags contain")[1].split(',')
    for bag in inside:
        if not "no other bags" in bag:
            bag = bag.replace('bags','').replace('bag','').replace('.','').strip()
            rules[main][' '.join(bag.split(' ')[1:] )] = int(bag.split(' ')[0])

part1()
part2()
