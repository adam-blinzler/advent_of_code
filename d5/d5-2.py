def binary_search(text,h,l,upper,lower):
    for r in text[:-1]:
        if r == upper:
            l = l + round((h-l)/2)
        elif r == lower:
            h = h - int((h-l)/2) - 1
            
    if text[-1] == upper:
        return h
    elif text[-1] == lower:
        return l

###################################
ids = [ binary_search(line.strip()[:7],128,0,'B','F')*8 +
        binary_search(line.strip()[7:],7,0,'R','L')
        for line in (open("input.txt"))]

ids.sort()
prev = 0
for id in ids:
    if prev + 2 == id:
        print("My seat id = ",id - 1)
        break
    else:
        prev = id

print("max id     = ",ids[-1])
