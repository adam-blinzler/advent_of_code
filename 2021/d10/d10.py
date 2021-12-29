
def calc_syntax_points(inputf, part = 1):
    get_points = {')' : 3,']' : 57,'}' : 1197,'>' : 25137}
    get_syntax_points = {'(' : 1,'[' : 2,'{' : 3,'<' : 4}

    get_closers = {'(':')','{':'}','[':']','<':'>'}
    syntax_points = list()
    points = 0
    with open(inputf) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            else:
                tracking = list()
                s_points = 0
                failed = False
                for c in list(line):
                    if tracking:
                        if c not in get_closers:
                            if c == get_closers[tracking[-1]]:
                                del tracking[-1]    
                            else:
                                points += get_points[c]
                                failed = True
                                break
                        else:
                            tracking.append(c)
                    else:
                        tracking.append(c)
                if not failed and tracking:
                    for c in reversed(tracking):
                        s_points *= 5
                        s_points += get_syntax_points[c]
                    syntax_points.append(s_points)
    if part == 2:
        mid = sorted(syntax_points)[int(len(syntax_points)/2)]
        print("Syntax points ",mid)
        return mid
    else:
        print("Syntax points ",points)
        return points

#####################################
    
print("-- Part 1")
assert calc_syntax_points("sample.txt") == 26397
assert calc_syntax_points("input.txt") == 387363

print("\n-- Part 2")
assert calc_syntax_points("sample.txt",2) == 288957
assert calc_syntax_points("input.txt",2) == 4330777059
