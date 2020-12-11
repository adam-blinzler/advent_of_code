adapters = sorted([int(x.strip()) for x in open("input.txt") if x.strip()])

print(adapters)

prev = 0
j_jmp = [0,0,0]

for a in adapters:
    if prev < a and a <= (prev + 3):
        j_jmp[(a-prev)-1] += 1
        prev = a
    else:
        print("chain brokend, did not use all adapters")
        break            

print("Maximum volatage is ", prev + 3)
print("    1 jolt differences", j_jmp[0]) 
print("    3 jolt differences", j_jmp[2]+1)
print("       multiplied = ",j_jmp[0] * (j_jmp[2]+1))
print("script done")
