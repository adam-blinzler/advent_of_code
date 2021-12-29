sample = {'x':[20,30],'y':[-10,-5]}
advent_input = {'x':[88,125],'y':[-157,-103]}


def did_we_land(vx, vy, target):
    x = 0
    y = 0
    
    while True:
        x += vx
        y += vy
        
        if target['x'][0] <= x <= target['x'][1] and target['y'][0] <= y <= target['y'][1]:
            return True
        elif x > target['x'][1] or y < target['y'][0]:
            return False

        if vx != 0:
            vx -= vx / abs(vx)
        vy -= 1

    return False

def find_min_vx(target):
    hitpoint = 0
    vx = 1
    while True:
        hitpoint += vx
        if target['x'][0] <= hitpoint <= target['x'][1]:
            break
        vx += 1
    return vx

def count_success(target):

    combos = 0

    for vx in range(find_min_vx(target),target['x'][1]+1):
        for vy in range(target['y'][0], -target['y'][0] + 1):
     
            if did_we_land(vx, vy, target):
                combos += 1

    print("Number of succesful launch velocities",combos)
    return combos

def find_ymax(target):
    '''
    if ymin is < 0
        y(t) will always return to 0
        1 timestep from 0 to ymin-1 will achieve max y(t)
    '''
    vy = -target['y'][0] - 1
    y = sum(list(range(vy+1)))

    print("Maximum hight, ",y)
    return y

#############################333

print("-- Part 1")
assert find_ymax(sample) == 45
assert find_ymax(advent_input) == 12246

print("\n-- Print 2")
assert count_success(sample) == 112
assert count_success(advent_input) == 3528
