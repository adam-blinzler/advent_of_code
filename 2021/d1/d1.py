
def check_depths(depths_file):
    count = 0
    with open(depths_file) as f:
        prev = int(f.readline().strip())
        while True:
            depth = f.readline()
            if not depth:
                break
            else:
                depth = int(depth.strip())
                if depth > prev:
                    count += 1
                prev = depth
    return count

def part1():
    assert check_depths("sample.txt") == 7
    print("Number of increases = " + str(check_depths("sample.txt")))
    print("Number of increases = " + str(check_depths("input.txt")))


def check_depths_sliding(depths_file,dims=3):
    sliding_list = list()
    count = 0
    with open(depths_file) as f:
        while True:
            depth = f.readline()
            if not depth:
                break
            else:
                depth = int(depth.strip())
                if len(sliding_list) == dims:
                    if sliding_list[1] + depth > sliding_list[0]:
                        count += 1
                    del sliding_list[0]
                for i in range(len(sliding_list)):
                    sliding_list[i] += depth
                sliding_list.append(depth)
    return count

def part2():
    assert check_depths_sliding("sample.txt") == 5
    print("Number of increases = " + str(check_depths_sliding("sample.txt")))
    print("Number of increases = " + str(check_depths_sliding("input.txt")))

print("-- PART 1")
part1()
print("-- PART 2")
part2()
