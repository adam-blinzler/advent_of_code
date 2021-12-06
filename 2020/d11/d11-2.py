import copy

def print_seating(s):
    print()
    for r in s:
        print(''.join(r))
    print()
    
def first_look(lst):
    for s in lst:
        if s == "#":
            return 1
        elif s == 'L':
            return 0
    return 0
    
def get_neighbors(seating, i,j):
    occupied = 0

    # look left
    occupied += first_look(reversed(seating[i][0:j]))

    # look right
    occupied += first_look(seating[i][j+1:])

    # look forward
    occupied += first_look(reversed([row[j] for row in seating[:i]]))

    # look back
    occupied += first_look([row[j] for row in seating[i+1:]])

    # look up left diagonal
    occupied += first_look([seating[i-ii][j-ii] for ii in range(1,min(i,j)+1)])

    # look up right diagonal
    occupied += first_look([seating[i-ii][j+ii] for ii in range(1,min(i,max_c-j)+1)])

    # look down left diagonal
    occupied += first_look([seating[i+ii][j-ii] for ii in range(1,min(max_r-i,j)+1)])

    # look down right diagonal
    occupied += first_look([seating[i+ii][j+ii] for ii in range(1,min(max_r-i,max_c-j)+1)])

    return occupied
    
def shuffle_seats(seating):
    any_changed = False
    new_seating = copy.deepcopy(seating)
    for i, row in enumerate(seating):
        for j, seat in enumerate(row):
            if seat in ['#','L']:
                n = get_neighbors(seating, i,j)
                if n >= 5 and seat == '#':
                    new_seating[i][j] = 'L'
                    any_changed = True
                elif n == 0 and seat == 'L':
                    new_seating[i][j] = '#'
                    any_changed = True  

    if any_changed:
        new_seating = shuffle_seats(new_seating)

    return new_seating

##########################333
sc = [list(s.strip()) for s in open("input.txt") if s.strip()]
max_r = len(sc) - 1
max_c = len(sc[0]) - 1

n_sc = shuffle_seats(sc)

occupied = 0
for s in n_sc:
    occupied += s.count("#")
    
print("Occupied seats =",occupied)
print("script done")
