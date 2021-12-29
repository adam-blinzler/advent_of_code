from collections import Counter # counts the frequency of elements in a list
# python 3.10+
from itertools import pairwise  # makes a list of all pairs (0,1) (1,2) (2,3) ...

def run_sub(abc_freq, pairs, sub_dict):
    new_pairs = dict()
    for p in pairs:
        if p in sub_dict:
            if p[0] + sub_dict[p] in new_pairs:
                new_pairs[p[0] + sub_dict[p]] += pairs[p]
            else:
                new_pairs[p[0] + sub_dict[p]] = pairs[p]

            if sub_dict[p] + p[1] in new_pairs:
                new_pairs[sub_dict[p] + p[1]] += pairs[p]
            else:
                new_pairs[sub_dict[p] + p[1]] = pairs[p]

            if sub_dict[p] in abc_freq:
                abc_freq[sub_dict[p]] += pairs[p]
            else:
                abc_freq[sub_dict[p]] = pairs[p]
    return abc_freq, new_pairs

def make_subs(template, steps):
    
    with open(template) as f:
        temp = f.readline().strip()
        f.readline() # throw away blank line
        sub_dict = dict()
        while True:
            line = f.readline().strip()
            if not line:
                break
            else:
                sub_dict[line.split(" -> ")[0]] = line.split(" -> ")[1]

    abc_freq = Counter(temp)
    pairs = Counter(map(''.join,pairwise(temp)))
    for _ in range(steps):
        abc_freq, pairs = run_sub(abc_freq, pairs, sub_dict)

    mm_diff = max(abc_freq.values()) - min(abc_freq.values())
    print("Max count - Min count",mm_diff)
    return mm_diff

print("-- Part 1")
assert make_subs("sample.txt",10) == 1588
assert make_subs("input.txt",10) == 2321

print("\n-- Part 2")
assert make_subs("sample.txt",40) == 2188189693529
assert make_subs("input.txt",40) == 2399822193707
