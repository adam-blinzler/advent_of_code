def example():
    return [1721, 979, 366, 299, 675, 1456]
    
def input_data():
    with open( "input.txt" ) as fl:
        nums = [ int(i) for i in fl.readlines() ]
    return nums
    
    
def find_it(nums):
    for idx in range(len(nums)):
        for idy in range(len(nums))[idx+1:]:
            for idz in range(len(nums))[idy+1:]:
                if (nums[idx] + nums[idy] + nums[idz] == 2020):
                    print("found it!")
                    found = True
                    print(nums[idx],",", nums[idy], ",", nums[idz])
                    print(nums[idx] * nums[idy] * nums[idz] )
                    return nums[idx] * nums[idy] * nums[idz]

def test_example():
    assert find_it(example()) == 241861950

find_it(input_data())

print ("script done")
