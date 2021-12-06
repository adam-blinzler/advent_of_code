
def calc_lantern(fish, days):
    f_counts = [0 for i in range(9)]
    for f in fish:
        f_counts[f] += 1
    
    for _ in range(days):
        n_counts = [0 for i in range(9)]
        for i in range(1,9):
            n_counts[i-1] = f_counts[i]
        n_counts[6] += f_counts[0]
        n_counts[8] = f_counts[0]
        f_counts = n_counts.copy()

    count = sum(f_counts)
    print("Number of fish {}".format(count))
        

    return count

def get_fish(report):
    with open(report) as f:
        return [int(n) for n in f.readline().split(',')]

print("-- Part 1")
assert calc_lantern(get_fish("sample.txt"), 18) == 26
assert calc_lantern(get_fish("sample.txt"),80) == 5934
assert calc_lantern(get_fish("input.txt"),80) == 373378

print("-- Part 2")
assert calc_lantern(get_fish("sample.txt"),256) == 26984457539
assert calc_lantern(get_fish("input.txt"),256) == 1682576647495
