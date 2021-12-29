def make_fold(line,spots):
    '''
    make he fold and return a unique list of spots
    '''
    _, ins = line.split("along ")
    if ins.split('=')[0] == 'x':
        idx = 0
    else:
        idx = 1
    fold = int(ins.split('=')[1])
    
    new_spots = list()
    for i, s in enumerate(spots):
        if s[idx] < fold:
            new_spots.append(s)
        elif s[idx] == fold:
            pass
        else:
            move = fold - (s[idx] - fold) # yes same as 2 * fold - s[idx]
            if move >= 0:
                if idx == 0:
                    new_spots.append((move, s[1]))
                else:
                    new_spots.append((s[0], move))

    return list(set(new_spots))

def read_in(in_file, part=1):
    with open(in_file) as f:
        # Get spots
        spots = list()
        while True:
            line = f.readline().strip()
            if not line:
                break
            else:
                x, y = line.split(',')
                spots.append((int(x),int(y)))
        '''
        Input file has a blank line between input segments
        '''
        # Make folds
        while True:
            line = f.readline().strip()
            if not line:
                break
            else:
                spots = make_fold(line, spots)

            # part 1 stops after 1 fold
            if part == 1:
                print("Number of spots visiable",len(spots))
                return len(spots)
    return spots

def print_spots(spots):
    width = max([s[0] for s in spots]) + 1
    tall =  max([s[1] for s in spots]) + 1
    for t in range(tall):
        row = ""
        for w in range(width):
            if (w,t) in spots:
                row += '#'
            else:
                row += '.'
        print(row)
    return

##########################################
print("-- Part 1")
assert read_in("sample.txt") == 17
assert read_in("input.txt") == 814

print("\n-- Part 2")
print_spots(read_in("sample.txt",2)) # O
print_spots(read_in("input.txt",2))  # PZEHRAER

