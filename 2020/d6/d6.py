def split(st): 
    return [c for c in st]

total = 0

with open( "input.txt" ) as fl:
    while True:
        reading = False
        lines = list()
        while True:
            line = fl.readline().strip()
            if not line:
                break
            lines.extend(split(line))
            reading = True

        if not reading:
            break
        
        lines = set(lines)
        total = total + len(lines)


print(total)
