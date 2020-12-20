from multiprocessing import Pool
from multiprocessing import freeze_support
import time
import functools
import itertools

def run_multiprocessing(func, a,i, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(functools.partial(func,a),i)

def get_new_point(point,delta):
    np = list()
    for p,d in zip(point,delta):
        np.append(p+d)
    return list(np)

def neighbor_offset():
    rng = list()
    for delta in itertools.product(range(-1, 2), repeat=4):
        rng.append(list(delta))
    return rng

def how_many_neighbors(active,point):
    total = 0
    for delta in neighbor_offset():
        if not (all(x == 0 for x in delta)):
            if get_new_point(point,delta) in active:
                total += 1
    return total

def check_point(active, sus_point):
    n = how_many_neighbors(active, sus_point)
    if n == 3:
        return sus_point
    elif n == 2:
        if sus_point in active:
            return sus_point
    return False


##################################
def main():
    rounds = 6
    n_processors = 7
    
    active = list()
    start = time.time()
    for y, line in enumerate(open("input.txt")):
        for x, item in enumerate(line.strip()):
            if item == '#':
                active.append([x,y,0,0])   

    for i in range(rounds):
        sus_points = list()
        for point in active:
            for delta in neighbor_offset():
                p = get_new_point(point,delta)
                if not p in sus_points:
                    sus_points.append(p)
        out = run_multiprocessing(check_point, active, sus_points, n_processors)

        active = list()
        for x in out:
            if x and not x in active:
                active.append(x)
        print(len(active))

    print("Active cubes ", len(active))
    print(time.time() - start)

if __name__ == "__main__":
    freeze_support()   # required to use multiprocessing
    main()
