'''
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg


   0  1  2  3  4  5  6  7  8  9
a  x     x  x     x  x  x  x  x
b  x           x  x        x  x
c  x  x  x  x  x        x  x  x
d        x  x  x  x  x     x  x
e  x     x        x  x     x 
f  x  x     x  x  x  x  x  x  x
g  x     x  x     x  x     x  x
'''

def get_easy_seg_count(filename):
    easy = [2,3,4,7]

    easy_segs = 0
    with open(filename) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            else:
                for seg in line.split('|')[1].split():
                    if len(seg) in easy:
                        easy_segs += 1
    print("Number of easy signals in {} is {}".format(filename, easy_segs))
    return easy_segs

def decode_fives(helper_rels, fives):
    decoded = dict()
    for f in fives:
        if helper_rels['1'][0] in f and helper_rels['1'][1] in f:
            decoded[f] = '3'
        elif helper_rels["4-1"][0] in f and helper_rels["4-1"][1] in f:
            decoded[f] = '5'
        else:
            decoded[f] = '2'
    return decoded

def decode_sixes(helper_rels, sixes):
    decoded = dict()
    for s in sixes:
        if not( helper_rels['1'][0] in s and helper_rels['1'][1] in s):
            decoded[s] = '6'
        elif helper_rels["4-1"][0] in s and helper_rels["4-1"][1] in s:
            decoded[s] = '9'
        else:
            decoded[s] = '0'

    return decoded

def decode_line(line):
    decoded = dict()
    helper_rels = dict()
    ## Decode simple digits
    easy = { 2 : '1', 3 : '7', 4 : '4', 7 : '8'}
    fives = list()
    sixes = list()
    for seg in line.split('|')[0].split():
        seg = ''.join(sorted(seg))
        if len(seg) in easy:
            decoded[seg] = easy[len(seg)]
            helper_rels[easy[len(seg)]] = seg
        elif len(seg) == 5:
            fives.append(seg)
        elif len(seg) == 6:
            sixes.append(seg)

    helper_rels["7-1"] = helper_rels['7']
    helper_rels["4-1"] = helper_rels['4']
    for n in helper_rels['1']:
        helper_rels["7-1"] = helper_rels["7-1"].replace(n,'')
        helper_rels["4-1"] = helper_rels["4-1"].replace(n,'')

    decoded.update(decode_fives(helper_rels,fives))
    decoded.update(decode_sixes(helper_rels,sixes))

    return decoded

def decoded_output(line):
    decoded = decode_line(line)
    output = ""
    for seg in line.split('|')[1].split():            
        output = output + decoded[''.join(sorted(seg))]
    return int(output)

def sum_all_outputs(filename):
    all_outputs = 0
    with open(filename) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            else:
                all_outputs += decoded_output(line)
    print("Sum of all outputs in {} is {}".format(filename,all_outputs))
    return all_outputs


print("-- Part 1")
assert get_easy_seg_count("sample.txt") == 26
assert get_easy_seg_count("input.txt") == 554

print("\n-- Part 2")
assert sum_all_outputs("sample.txt") == 61229
assert sum_all_outputs("input.txt") == 990964
