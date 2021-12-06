def read_nav(nav_file):
    nav = {"pos" : 0, "depth" : 0, "aim" : 0}
    with open(nav_file) as f:
        while True:
            info = f.readline()
            if not info:
                break
            else:
                direction, steps = info.strip().split(" ")
                steps = int(steps)
                if direction == "forward":
                    nav["pos"] += steps
                    nav["depth"] += nav["aim"] * steps
                elif direction == "down":
                    nav["aim"] += steps
                elif direction == "up":
                    nav["aim"] -= steps
    return nav

def part1_answer(nav_file):
    nav = read_nav(nav_file)
    return nav["pos"] * nav["aim"]

def part2_answer(nav_file):
    nav = read_nav(nav_file)
    return nav["pos"] * nav["depth"]

print("-- Part 1")
assert part1_answer("sample.txt") == 150
print("sample = " + str(part1_answer("sample.txt")))
print("input  = " + str(part1_answer("input.txt")))

print("-- Part 2")
assert part2_answer("sample.txt") == 900
print("sample = " + str(part2_answer("sample.txt")))
print("input  = " + str(part2_answer("input.txt")))
