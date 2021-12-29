def get_octopi_list(oct_file):
    octopi = list()
    with open(oct_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            octopi.append([int(loc) for loc in list(line)])
    return octopi
    
def run_sim(octopi, gotime, part = 1):

    window = [(i,j) for i in range(10) for j in range(10)]
    flash_cnt = 0
    for itr_cnt in range(gotime):
        for loc in window:
            octopi[loc[0]][loc[1]] += 1

        flash = True
        flashes = list()
        while flash:
            flash = False
            for loc in window:
                i = loc[0]
                j = loc[1]
                if octopi[i][j] > 9 and (i,j) not in flashes:
                    flash = True
                    flashes.append((i,j))

                    octopi[i][j] += 1

                    adjacent = [(i-1,j-1),(i-1,j),(i-1,j+1), 
                                  (i,j-1),          (i,j+1),
                                (i+1,j-1),(i+1,j),(i+1,j+1)]
                    for nloc in adjacent:
                        if nloc[0] >=0 and nloc[0] <= 9 and nloc[1] >=0 and nloc[1] <= 9:
                            octopi[nloc[0]][nloc[1]] += 1

        if part == 2 and len(flashes) > 99:
            print("All flash on step",itr_cnt+1)
            return itr_cnt+1

        flash_cnt += len(flashes)
        for loc in flashes:
            octopi[loc[0]][loc[1]] = 0

    print("Flashes seen",flash_cnt)
    return flash_cnt

#############################
print("-- Part 1")
assert run_sim(get_octopi_list("sample.txt"),100) == 1656
assert run_sim(get_octopi_list("input.txt"),100) == 1755

print("\n-- Part 2")
# 500 is just a randomly large number more than expected outcome
assert run_sim(get_octopi_list("sample.txt"),500,2) == 195
assert run_sim(get_octopi_list("input.txt"),500,2) == 212
