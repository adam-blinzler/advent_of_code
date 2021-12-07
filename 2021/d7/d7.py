import statistics
import math
from copy import deepcopy

def get_crab_list(crab_file):
    with open(crab_file) as f:
        crab_pos = [ int(c) for c in f.readline().strip().split(',')]
    return crab_pos

def find_crab_median(crab_file):
    crab_pos = get_crab_list(crab_file)
    c_median = int(statistics.median(crab_pos))

    print("Best location {}".format(c_median))
    crab_cost = sum([abs(crab - c_median) for crab in crab_pos])

    print("  Cost to move is {}".format(crab_cost))
    return crab_cost

def part2_cost(crab_pos, c_mean):
    return sum([sum(range(abs(crab - c_mean)+1)) for crab in crab_pos if crab != c_mean])

def find_crab_mean(crab_file):
    crab_pos = get_crab_list(crab_file)
    c_means = [math.floor(statistics.mean(crab_pos)), math.ceil(statistics.mean(crab_pos))]

    crab_cost = min([part2_cost(crab_pos,c) for c in c_means])
    #print("Best location {}".format())

    print("  Cost to move is {}".format(crab_cost))
    return crab_cost


print("-- Part 1")
assert find_crab_median("sample.txt") == 37
assert find_crab_median("input.txt") == 344605

print("\n-- Part 2")
assert find_crab_mean("sample.txt") == 168
assert find_crab_mean("input.txt") == 93699985

