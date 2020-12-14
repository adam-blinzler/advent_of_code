def apply_mask(mask,mem):
    new_mem = list()
    for ms, mm in zip(mask, mem):
        if ms == 'X':
            new_mem.append(str(mm))
        else:
            new_mem.append(str(ms))
    return int(''.join(new_mem),2)

def bitfield(n,l=0):
    bf = [1 if d=='1' else 0 for d in bin(n)[2:]]
    if (36 - len(bf)) > 0:
        bf = ['0'] * (36 - len(bf)) + bf
    return bf


#####################################
mem = dict()

for line in open("input.txt"):
    if "mask" in line:
        mask = list(line.strip().split(" = ")[1])
    else:
        loc = int(line.strip().split(" = ")[0].replace("mem[",'').replace(']',''))
        mem[loc] = int(line.strip().split(" = ")[1])
        mem[loc] = apply_mask(mask,bitfield(mem[loc],36))



s_mem = 0
for k in mem:
    s_mem += mem[k]
print("Sum of all memory locations = ",s_mem)
