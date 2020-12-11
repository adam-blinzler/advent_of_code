def get_max():
    prev = 0
    for a in adapters:
        if prev < a and a <= (prev + 3):
            prev = a
        else:
            print("chain brokend, did not use all adapters")
            break
    return a +3

def get_sols():
    sols = {0:1}
    for a in adapters:
        sols[a] = 0
        if a - 1 in sols:
            sols[a]+=sols[a-1]
        if a - 2 in sols:
            sols[a]+=sols[a-2]
        if a - 3 in sols:
            sols[a]+=sols[a-3]
    return sols[adapters[-1]]

######################
adapters = sorted([int(x.strip()) for x in open("input.txt") if x.strip()])

print("1) ",get_max())


print("2) ",get_sols())

print("script done")
