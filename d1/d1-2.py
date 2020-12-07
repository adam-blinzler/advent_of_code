found = False
with open( "input.txt" ) as fl:
    nums = [ int(i) for i in fl.readlines() ]

for idx in range(len(nums)):
    for idy, _ in enumerate(nums[idx+1:]):
        for idz, _ in enumerate(nums[idy+1:]):
            if (nums[idx] + nums[idy] + nums[idz] == 2020):
                print("found it!")
                found = True
                print(nums[idx],",", nums[idy], ",", nums[idz])
                print(nums[idx] * nums[idy] * nums[idz] )
                break;
        if found:
            break;
    if found:
        break;

print ("script done")
