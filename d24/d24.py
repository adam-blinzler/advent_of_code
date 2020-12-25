from copy import deepcopy as dc

def get_neighbors(cords):
    return [ (cords[0]+delta[0], cords[1]+delta[1]) for delta in [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]]
        
def parse_placement(line):
    ns = 0
    we = 0

    i = 0
    while i < len(line):
        char = line[i]
        if char == 'e':
            we += 1
        elif char == 'w':
            we -= 1
        else:
            # Note in this hex grid, N and S are not possible options
            char = char + line[i+1] 
            i += 1
            if char == 'ne':
                ns -=1
                we += 1
            elif char == 'nw':
                ns -= 1
            elif char == 'se':
                ns +=1
            elif char == 'sw':
                ns += 1
                we -= 1
        i += 1
    return (ns, we)

###################################
tiles = dict()
for line in open("input.txt"):
    line = list(line.strip())
    tile = parse_placement(line)
    if not tile in tiles.keys():
        tiles[tile] = True
    else:
        tiles[tile] = not tiles[tile]

print("Day 0: ",sum(v for _, v in tiles.items()))

for i in range(100):
    new_tiles = dc(tiles)
    for t in tiles:
        for cord in get_neighbors(t):
            if not cord in new_tiles:
                new_tiles[cord] = False

    for t, black in new_tiles.items():
        count_black = sum(1 for n_cord in get_neighbors(t)
                          if n_cord in tiles and tiles[n_cord])

        if black and (count_black == 0 or count_black > 2):
            new_tiles[t] = False
        elif not black and count_black == 2:
            new_tiles[t] = True
    tiles = dc(new_tiles)
    
print("Day {}: {}".format(i+1,sum(v for _, v in tiles.items())))
