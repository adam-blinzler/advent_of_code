def find_loop_size(target):
    loop_size = 0
    c = 1
    while True:
        loop_size += 1
        c *= 7
        c = c % 20201227
        if c == target:
            return loop_size

def transform_loop(public, loop_size):
    c = 1
    for _ in range(loop_size):
        c *= public
        c = c % 20201227
    return c

####################
with open("input.txt") as f:
    c_public = int(f.readline().strip())
    d_public = int(f.readline().strip())

c_loop = find_loop_size(c_public)
d_loop = find_loop_size(d_public)

print("Card loop size :",c_loop)
print("Door loop size :",d_loop)

c_secret = transform_loop(c_public,d_loop)
d_secret = transform_loop(d_public,c_loop)
if c_secret == d_secret:
    print("Secret key matched :",d_secret)
else:
    print("Something went wrong!")
    print("Card secrete was :", c_secret)
    print("Door secrete was :", d_secret)
