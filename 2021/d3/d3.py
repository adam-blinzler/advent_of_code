#!/usr/bin/env python


def find_counts(report):
    count = list()
    with open(report) as f:
        while True:
            diag = f.readline()
            if not diag:
                break
            else:
                diag = diag.strip()
                for i, bit in enumerate(diag):
                    if i+1 > len(count):
                        count.append([0,0])
                    count[i][int(bit)] += 1
    return count

def calc_power(counts):
    epsilon = '0b'
    sigma = '0b'
    for i, j in counts:
        if i > j:
            epsilon = epsilon + '0'
            sigma = sigma + '1'
        else:
            epsilon = epsilon + '1'
            sigma = sigma + '0'

    return int(epsilon,2) * int(sigma,2)

def get_filter(all_diag, idx, part):
    counts = [0,0]
    for diag in all_diag:
        if diag[idx] == '0':
            counts[0] += 1
        else:
            counts[1] += 1

    if part == "oxygen":
        if counts[0] > counts[1]:
            filter = '0'
        else:
            filter = '1'
    elif part == "co2":
        if counts[0] <= counts[1]:
            filter = '0'
        else:
            filter = '1'

    return filter

def get_diag(all_diag, part):
    for idx in range(len(all_diag[0])):
        filter = get_filter(all_diag, idx, part)
        for diag in list(all_diag):
            if diag[idx] != filter:
                all_diag.remove(diag)

        if len(all_diag) == 1:
            break
    return all_diag[0]

def part2(report):
    with open(report) as f:
        all_diag = f.read().splitlines()
    oxygen = get_diag(all_diag.copy(), "oxygen")
    co2 = get_diag(all_diag.copy(), "co2")
    life = int('0b'+oxygen,2) *int('0b'+co2,2)
    print("Life support is {}".format(life))
    return life

def part1(report):
    counts = find_counts(report)
    power = calc_power(counts)
    print("Power comsumption is {}".format(power))
    return power

print("-- Part 1")
assert part1("sample.txt") == 198
assert part1("input.txt") == 841526

print("\n-- Part 2")
assert part2("sample.txt") == 230
assert part2("input.txt") == 4790390
