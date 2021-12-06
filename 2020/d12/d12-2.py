wp = [10,1]
md = [0,0]

facing = "E"

def rotate(dr, val):
    global wp
    
    if dr == "L" and val == 90 or dr == "R" and val == 270:
        wp[0], wp[1] = -wp[1], wp[0]
    elif dr == "L" and val == 270 or dr == "R" and val ==90:
        wp[0], wp[1] = wp[1], -wp[0]
    elif dr == "L" and val == 180 or dr == "R" and val == 180:
        wp[0], wp[1] = -wp[0], -wp[1]

def move(dr, val):
    global facing
    
    if dr == 'N':
        wp[1] += val
    elif dr == 'S':
        wp[1] -= val
    elif dr == 'E':
        wp[0] += val
    elif dr == 'W':
        wp[0] -= val
    elif dr in ['L','R']:
        rotate(dr,val)
    elif dr == 'F':
        md[0] += (wp[0] * val)
        md[1] += (wp[1] * val)

##############################

for l in open("input.txt"):
    move(list(l)[0], int(''.join(list(l.strip())[1:])))
    
print("Manhattan distance =", abs(md[0]) + abs(md[1]))

