import itertools as it
import os
import sys

class vent:
    def __init__(self, text):
        self.print_line = text
        
        p1, p2 = text.split(" -> ")
        self.x1 = int(p1.split(',')[0])
        self.y1 = int(p1.split(',')[1])
        self.x2 = int(p2.split(',')[0])
        self.y2 = int(p2.split(',')[1])

        if self.x1 == self.x2 or self.y1 == self.y2:
            self.part1 = True
        else:
            self.part1 = False

def get_lines(report):
    vent_lines = list()
    with open(report) as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                vent_lines.append(vent(line.strip()))
    return vent_lines

def format_point_name(cord):
    return "{},{}".format(cord[0],cord[1])

def get_points(line):
    points = list()
    if line.part1:
        for x in range(min(line.x1,line.x2),max(line.x1,line.x2)+1):
            for y in range(min(line.y1,line.y2),max(line.y1,line.y2)+1):
                points.append([x,y])
    else:
        dx = int(line.x2>line.x1) or -1
        dy = int(line.y2>line.y1) or -1
        for dp in range(abs(line.x2-line.x1)+1):
            points.append([line.x1 + dx*dp, line.y1 + dy*dp])
    return points

def calc_points(vent_lines):
    pts = dict()
    for line in vent_lines:
        for cord in get_points(line):
            if not format_point_name(cord) in pts:
                pts[format_point_name(cord)] = 1
            else:
                pts[format_point_name(cord)] += 1

    # could not even need pts dict and do counting above, harder to debug
    count = 0
    for name, pt in pts.items():
        if pt >= 2:
            count += 1
  
    return count
####################################################
os.chdir(os.path.dirname(sys.argv[0]))

print("-- Part 1")
p1_sample = calc_points([l for l in get_lines("sample.txt") if l.part1])
assert p1_sample == 5
print(p1_sample)

p1_input = calc_points([l for l in get_lines("input.txt") if l.part1])
assert p1_input == 5774
print(p1_input)


print("-- Part 2")
p2_sample = calc_points(get_lines("sample.txt"))
assert p2_sample == 12
print(p2_sample)

p2_input = calc_points(get_lines("input.txt"))
assert p2_input == 18423
print(p2_input)
