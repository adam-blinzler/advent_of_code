with open( "input.txt" ) as fl:
    passwords = fl.readlines()

good_pswd = 0
for p in passwords:
    check = p.split(':')[0].split(' ')[1].strip()
    c_1 = int(p.split(':')[0].split(' ')[0].split('-')[0]) - 1 
    c_2 = int(p.split(':')[0].split(' ')[0].split('-')[1]) - 1
    pswd = p.split(':')[1].strip()
    if (pswd[c_1] == check) and (pswd[c_2] != check):
        good_pswd = good_pswd + 1
    elif (pswd[c_1] != check) and (pswd[c_2] == check):
        good_pswd = good_pswd + 1

print(good_pswd)
print("script done")