import copy

def print_seating(s):
    print()
    for r in s:
        print(''.join(r))
    print()
    
def get_neighbors(seating, i,j):
    if i == 0:
        i_ops = [0,+1]
    elif i == max_r:
        i_ops = [-1,0]
    else:
        i_ops = [-1,0,+1]
    if j == 0:
        j_ops = [0,+1]
    elif j == max_c:
        j_ops = [-1,0]
    else:
        j_ops = [-1,0,+1]        

    occupied = 0
    for ii in i_ops:
        for jj in j_ops:
            if ii == 0 and jj == 0:
                continue
            if seating[i + ii][j + jj] == '#':
                occupied += 1
    return occupied
    
def shuffle_seats(seating):
    any_changed = False
    new_seating = copy.deepcopy(seating)
    for i, row in enumerate(seating):
        for j, seat in enumerate(row):
            if seat in ['#','L']:
                n = get_neighbors(seating, i,j)
                if n >= 4 and seat == '#':
                    new_seating[i][j] = 'L'
                    any_changed = True
                elif n == 0 and seat == 'L':
                    new_seating[i][j] = '#'
                    any_changed = True

    #print_seating(new_seating)
    if any_changed:
        new_seating = shuffle_seats(new_seating)

    return new_seating

##########################333
sc = [list(s.strip()) for s in open("input.txt") if s.strip()]
max_r = len(sc) - 1
max_c = len(sc[0]) - 1

n_sc = shuffle_seats(sc)
print_seating(n_sc)

occupied = 0
for s in n_sc:
    occupied += s.count("#")
    
print("Occupied seats",occupied)
