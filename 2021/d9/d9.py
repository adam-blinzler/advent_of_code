import math

def get_heightmap(input):
    hmap = list()
    with open(input) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            else:
                hmap.append([int(s) for s in line])
    return hmap

def min_max(hmap):
    i_min = 0
    i_max = len(hmap) - 1
    j_min = 0
    j_max = len(hmap[0]) - 1
    return i_min, i_max, j_min, j_max 

def calc_lows(hmap, part=1):
    i_min, i_max, j_min, j_max = min_max(hmap)
    low_spots = list()
    for i, _ in enumerate(hmap):
        for j, spot in enumerate(hmap[i]):    
            check_spots = list()
            if i - 1 >= i_min:
                check_spots.append(hmap[i-1][j])
            if j - 1 >= j_min:
                check_spots.append(hmap[i][j-1])
            if i + 1 <= i_max:
                check_spots.append(hmap[i+1][j])
            if j + 1 <= j_max:
                check_spots.append(hmap[i][j+1])
            if all([spot < s for s in check_spots]):
                low_spots.append(spot)
                
    total_risk = sum([s+1 for s in low_spots])
    print("Total risk is ",total_risk)
    return total_risk

def merge_matches(basins, matches):
    '''
    Merge basins that matched into min matches
    '''
    merge_basin = min(matches)
    matches.remove(merge_basin)
    for m in matches:
        basins[merge_basin].extend(basins[m])
        del basins[m]

    basins[merge_basin] = list(set(basins[merge_basin]))    
    return basins

def assign_to_basin(hmap, basins, i, j):
    
    i_min, i_max, j_min, j_max = min_max(hmap)    
    check_cords = list()
    if i - 1 >= i_min:
        check_cords.append((i-1,j))
    if j - 1 >= j_min:
        check_cords.append((i,j-1))
    if i + 1 <= i_max:
        check_cords.append((i+1,j))
    if j + 1 <= j_max:
        check_cords.append((i,j+1))

    matches = list()
    for idx, b in enumerate(basins):
        for cord in b:
            if cord in check_cords:
                if idx not in matches:
                    basins[idx].append((i,j))
                    matches.append(idx)
                break

    if not matches:
        basins.append([(i,j)])
    else:
        basins = merge_matches(basins, matches)

    return basins

def calc_basins(hmap):
    basins = list()
    for i, _ in enumerate(hmap):
        for j, spot in enumerate(hmap[i]):
            if spot != 9:
                basins = assign_to_basin(hmap,basins,i,j)
    prod = math.prod(sorted([len(b) for b in basins])[-3:])
    print("Product of highest 3 basins ", prod)
    return prod

###################################
print("-- Part 1")
assert calc_lows(get_heightmap("sample.txt")) == 15
assert calc_lows(get_heightmap("input.txt")) == 550

print("-- Part 2")
assert calc_basins(get_heightmap("sample.txt")) == 1134
assert calc_basins(get_heightmap("input.txt")) == 1100682
