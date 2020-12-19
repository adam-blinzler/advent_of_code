def neighbor_offset():
    rng = list()
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                rng.append([dx,dy,dz])
    return rng

def how_many_neighbors(active,point):
    total = 0
    for x,y,z in neighbor_offset():
        if not ( x == 0 and y == 0 and z == 0 ):
            if [point[0]+x,point[1]+y,point[2]+z] in active:
                total += 1
    return total

##################################
rounds = 6

active = list()

for y, line in enumerate(open("input.txt")):
    for x, item in enumerate(line.strip()):
        if item == '#':
            active.append([x,y,0])   

for i in range(rounds):
    new_active = list()
    for point in active:
        for x,y,z in neighbor_offset():
            sus_point = [point[0]+x,point[1]+y,point[2]+z]
            n = how_many_neighbors(active, sus_point)
            if n == 3:
                if not sus_point in new_active:
                    new_active.append(sus_point)
            elif n == 2:
                if x == 0 and y == 0 and z == 0:
                    if not sus_point in new_active:
                        new_active.append(sus_point)   
    active = new_active

print("Active cubes ", len(active))
