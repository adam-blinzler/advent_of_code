
def example():
    return [1721, 979, 366, 299, 675, 1456]

def input_data():
    with open( "input.txt" ) as fl:
        nums = [ int(i) for i in fl.readlines() ]
    return nums

def find_it(nums):
    for idx in range(len(nums)):
        for idy in range(len(nums))[idx+1:]:
            if (nums[idx] + nums[idy] == 2020):
                print("found it!")
                print(nums[idx],",", nums[idy])
                print(nums[idx] * nums[idy])
                return nums[idx] * nums[idy]

def test_example():
    assert find_it(example()) == 514579

find_it(input_data())

print ("script done")
