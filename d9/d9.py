def is_valid(sus, check_list):
    for i, n in enumerate(check_list[:-1]):
        for j in check_list[i+1:]:
            if (n + j) == sus:
                return True
    return False

#############################
all_nums = [int(f.strip()) for f in open("input.txt") if f.strip()]
    
rolling = 25
for i in range(rolling, len(all_nums)):
    if not is_valid(all_nums[i],all_nums[i-rolling:i]):
        print("1) Number not a sum of the previous - ", all_nums[i])
        break

for j in range(i-1,0,-1):
    cont = list()
    for k in range(j,0,-1):
        cont.append(all_nums[k])
        sum_cont = sum(cont)
        if sum_cont == all_nums[i]:
            print("2) Min and max of list are ",min(cont),max(cont))
            print("     their sum is = ", min(cont) + max(cont))
        elif sum_cont > all_nums[i]:
            break

print("script done")
