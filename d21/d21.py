def remove_i_from_a(ing,safe):
    hits = False
    for a, ings in allergies.items():
        if ing in ings and not a == safe:
            del allergies[a][allergies[a].index(ing)]
            hits = True
    return hits

def solve_allergies():
    hits = True
    while hits:
        hits = False
        for a, ings in allergies.items():
            if len(ings) == 1:
                hits = hits or remove_i_from_a(ings[0],a)
    return   

def unique_allergies(ings):
    return [i for i in ings if i in allergies[a]]

def populate_ingredients():
    for k, v in allergies.items():
        ingredients[v[0]] = k

def total_inert():
    total = 0
    for p in products:
        for ing in p.split():
            if ingredients[ing] == '':
                total += 1
    return total

def i_from_a():
    return ','.join([i[0] for a,i in sorted(allergies.items())])

########################33
allergies = dict()
ingredients = dict()
products = list()

for line in open("input.txt"):    
    ii, aa = line.strip().split(" (contains ")
    products.append(ii)
    for i in ii.split():
        if not i in ingredients:
            ingredients[i] = ''

    for a in aa[:-1].split(', '):
        if a in allergies:
            allergies[a] = unique_allergies(ii.split())
        else:
            allergies[a] = list(ii.split())

solve_allergies()
populate_ingredients()

print("1) Number of inert ingredients = ", total_inert())
print("2) All allergy ingredients = ", i_from_a())

