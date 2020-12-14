import copy

def float_addr(addr, val, idx):
    if not 'X' in addr:
        mem[int(''.join(addr),2)] = val
    else:
        for i in range(idx,len(addr)):
            if addr[i] == 'X':
                n_addr = copy.deepcopy(addr)
                n_addr[i] = '0'
                float_addr(n_addr,val,i+1)
                n_addr[i] = '1'
                float_addr(n_addr,val,i+1)
                
def apply_mask(mask,addr):
    new_addr = list()
    for ms, ad in zip(mask, addr):
        if ms == 'X':
            new_addr.append(str(ms))
        elif ms == '0':
            new_addr.append(str(ad))
        elif ms == '1': 
            new_addr.append(str(ms))

    return new_addr

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
        loc = apply_mask(mask,bitfield(loc,36))
        float_addr(loc, int(line.strip().split(" = ")[1]), 0)
        
#print(mem)
print("Sum of all memory locations = ",sum(mem.values()))
