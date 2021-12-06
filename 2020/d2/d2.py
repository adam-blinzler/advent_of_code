with open( "input.txt" ) as fl:
    passwords = fl.readlines()

good_pswd = 0
for p in passwords:
    check = p.split(':')[0].split(' ')[1]
    c_min = int(p.split(':')[0].split(' ')[0].split('-')[0])
    c_max = int(p.split(':')[0].split(' ')[0].split('-')[1])
    pswd = p.split(':')[1]
    if (pswd.count(check) >= c_min) and (pswd.count(check)<= c_max):
        good_pswd = good_pswd + 1

print(good_pswd)
print("script done")
