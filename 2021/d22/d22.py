def cubes(ins_file):
    cubes = dict()
    with open(ins_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            else:
                tp = line.split()[0]
                x1 = int(line.split()[1].split(',')[0].split('=')[1].split("..")[0])
                x2 = int(line.split()[1].split(',')[0].split('=')[1].split("..")[1])

                y1 = int(line.split()[1].split(',')[1].split('=')[1].split("..")[0])
                y2 = int(line.split()[1].split(',')[1].split('=')[1].split("..")[1])

                z1 = int(line.split()[1].split(',')[2].split('=')[1].split("..")[0])
                z2 = int(line.split()[1].split(',')[2].split('=')[1].split("..")[1])

                x_low = min(x1,x2) 
                if x_low < -50:
                    x_low = -50
                x_high = max(x1,x2) 
                if x_high > 50:
                    x_high= 50

                y_low = min(y1,y2) 
                if y_low < -50:
                    y_low = -50
                y_high = max(y1,y2) 
                if y_high > 50:
                    y_high= 50

                z_low = min(z1,z2) 
                if z_low < -50:
                    z_low = -50
                z_high = max(z1,z2) 
                if z_high > 50:
                    z_high= 50

                for x in range(x_low,x_high+1):
                    for y in range(y_low,y_high+1):
                        for z in range(z_low,z_high+1):
                            if tp == 'on':
                                cubes[(x,y,z)] = True
                            elif tp == 'off' and (x,y,z) in cubes:
                                del cubes[(x,y,z)]

    print(len(cubes.keys()))
    return len(cubes.keys())

print("-- Part 1")
assert cubes("sample1.txt") == 39
assert cubes("sample2.txt") == 590784
assert cubes("input.txt") == 600458
