# Should probably not open the file each time
def get_trees(mc, mr):
# Only works for move to right operations
    trees = 0
    row = 0
    col = 0
    with open( "input.txt" ) as fl:
        line = fl.readline().strip()
        while True:
            for i in range(mr):
                line = fl.readline().strip()
                row = row + 1
            if not line:
                break

            col = col + mc
            if col >= len(line):
                col = (col % len(line))
            if line[col] == '#':
                trees = trees + 1
    return tree

mult = 0
for c , r in [[1,1], [3,1], [5,1], [7,1], [1,2]]:
    num_trees = get_trees(c, r)
    if num_trees > 0:
        if mult == 0:
            mult = numtrees
        else:
            mult = mult * numtrees

print(mult)
print("done")
