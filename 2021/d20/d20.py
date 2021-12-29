class image:
    def __init__(self, mx, img, enh):
        self.mins = 0
        self.maxs = mx
        self.img = img
        self.enh = enh
        self.default = '0'
        
    def enhance(self):
        self.mins -= 1
        self.maxs += 1

        influence = [(-1,-1),(0,-1),(1,-1),
                     (-1, 0),(0, 0),(1, 0),
                     (-1, 1),(0, 1),(1, 1)]

        new_image = dict()
        for py in range(self.mins-1, self.maxs+2):
            for px in range(self.mins-1, self.maxs+2):
                enh_lookup = ''
                for ox, oy in influence:
                    if (px+ox,py+oy) in self.img:
                        enh_lookup += '1'
                    elif px+ox < self.mins or px+ox > self.maxs or py+oy < self.mins or py+oy > self.maxs:
                        enh_lookup += self.default
                    else:
                        enh_lookup += '0'
                if self.enh[int(enh_lookup,2)] == '#':
                    new_image[(px,py)] = True

        self.img = new_image

        return 
    
    def print_img(self):
        print(self.img)
        for y in range(self.mins,self.maxs):
            line = ''
            for x in range(self.mins,self.maxs):
                if (x,y) in self.img:
                    line += '#'
                else:
                    line += '.'
            print(line)
        return
    
def import_image(ifile):
    img = dict()

    with open(ifile) as f:
        enh = list(f.readline().strip())
        f.readline()
        row = 0
        while True:
            line = f.readline().strip()
            if not line:
                break
            else:
                for col, ch in enumerate(line):
                    if ch == '#':
                        img[(col,row)] = True
            row += 1
    return image(row, img, enh)

def make_the_rounds(img_file, rounds):
    image_class = import_image(img_file)
    for i in range(rounds):
        if image_class.enh[0] == "." or i % 2 == 0:
            image_class.default = "0"
        else:
            image_class.default = "1" 
        image_class.enhance()
    
    print(len(image_class.img))
    return len(image_class.img)


################################
print("-- Part 1")
assert make_the_rounds("sample.txt",2) == 35
assert make_the_rounds("input.txt",2) == 5179

print("\n-- Part 2")
assert make_the_rounds("sample.txt",50) == 3351
assert make_the_rounds("input.txt",50) == 16112
