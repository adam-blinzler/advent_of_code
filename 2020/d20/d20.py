class tile:
    def __init__(self,number):
        self.id = number
        self.layout = list()
        # like a clock - top, right, bottom, left
        self.edges = [0]*8
        self.mates = [0]*8

    def hash_edges(self):
        #store both non and flipped. Doesn't matter as they are unique both ways
        self.edges[0] = int(self.layout[0].replace('.','0').replace('#','1'),2)
        self.edges[1] = int(self.layout[0].replace('.','0').replace('#','1')[::-1],2)

        self.edges[2] = int(''.join([s[-1] for s in self.layout]).replace('.','0').replace('#','1'),2)
        self.edges[3] = int(''.join([s[-1] for s in self.layout]).replace('.','0').replace('#','1')[::-1],2)

        self.edges[4] = int(self.layout[-1].replace('.','0').replace('#','1'),2)
        self.edges[5] = int(self.layout[-1].replace('.','0').replace('#','1')[::-1],2)

        self.edges[6] = int(''.join([s[0] for s in self.layout]).replace('.','0').replace('#','1'),2)
        self.edges[7] = int(''.join([s[0] for s in self.layout]).replace('.','0').replace('#','1')[::-1],2)

def find_all_mates():
    for t0,c0 in tiles.items():
        for t1,c1 in tiles.items():
            if t0 == t1:
                continue
            for j, e0 in enumerate(c0.edges):
                if c0.mates[j] > 0:
                    continue
                for i, e1 in enumerate(c1.edges):
                    if c1.mates[i] > 0:
                        continue
                    elif e0 == e1:
                        c0.mates[j] = t1
                        c1.mates[i] = t0
                        break

############
tiles = dict()
for line in open("input.txt"):
    line = line.strip()
    if "Tile" in line:
        number = int(line.split()[1].replace(':','').strip())
        tiles[number] = tile(number)
    elif not line:
        tiles[number].hash_edges()
    else:
        tiles[number].layout.append(line)
tiles[number].hash_edges()

find_all_mates()

corners = 1
for t,c in tiles.items():
#    print(t,c.mates)
    if c.mates.count(0) == 4:
        corners *= t
        
print("All corners multiplied = ",corners)
