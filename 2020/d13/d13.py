
def part1():
    with open("input.txt") as fl:
        ts = int(fl.readline().strip())
        buses = [int(x) for x in fl.readline().strip().replace('x,','').split(',')]

    depart = 1000
    for b in buses:
        dp = (b - ts % b)
        if dp < depart:
            print("ID of earliest departing bus",b * dp)
            depart = dp

#######################################
part1()


with open("i1.txt") as fl:
    fl.readline()
    buses = fl.readline().strip().split(',')







        
print("script done")
