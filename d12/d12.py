md = [0,0]

facing = "E"

def rotate(cw, val):
    idx = 4 + cw * int((val/90) % 4)
    mv = ['E','S','W','N']
    c = mv.index(facing)
    return mv[(idx + c) % 4]

def move(dr, val):
    global ew
    global ns
    global facing
    
    if dr == 'N':
        md[1] += val
    elif dr == 'S':
        md[1] -= val
    elif dr == 'E':
        md[0] += val
    elif dr == 'W':
        md[0] -= val
    elif dr == 'L':
        facing = rotate(-1,val)
    elif dr == 'R':
        facing = rotate(+1,val)
    elif dr == 'F':
        move(facing,val)
        

##############################

for l in open("input.txt"):
    move(list(l)[0], int(''.join(list(l.strip())[1:])))

print("Manhattan distance =", abs(md[0]) + abs(md[1]))

