# do without intertools

def example():
    return [1721, 979, 366, 299, 675, 1456]

def input_data():
    with open( "input.txt" ) as fl:
        nums = [ int(i) for i in fl.readlines() ]
    return nums

def find_product(depth, nums, idx = []):
    nums_range = range(len(nums))
    
    if idx:
        for j in nums_range[idx[-1]+1:]:
            if depth == 0:
                s = nums[j]
                for i in idx:
                    s = s + nums[i]

                if s == 2020:
                    p = nums[j]
                    st = str(nums[j])
                    for i in idx:
                        p = p * nums[i]
                        st = str(nums[i]) + ' * ' + st

                    print("found it!")
                    print(st, "=", p)
                    return p
            else:    
                p = find_product(depth - 1, nums, idx + [j])
                if p:
                    return p
    else:
        for j in nums_range:
            p = find_product(depth - 1, nums, [j])
            if p:
                return p
    return None

def test_example1():
    assert find_product(1,example()) == 514579

def test_example2():
    assert find_product(2,example()) == 241861950

find_product(1, input_data())
find_product(2, input_data())
print("done")
