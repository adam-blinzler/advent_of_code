found = False
with open( "input.txt" ) as fl:
    nums = [ int(i) for i in fl.readlines() ]

for idx in range(len(nums)):
    for idy, _ in enumerate(nums[idx+1:]):
        if (nums[idx] + nums[idy] == 2020):
            print("found it!")
            found = True
            print(nums[idx],",", nums[idy])
            print(nums[idx] * nums[idy])
            break;
    if found:
        break;

print ("script done")
