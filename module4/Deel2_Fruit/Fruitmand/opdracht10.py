from fruitmand import fruitmand

fruitmand.sort(reverse = True, key = lambda gewicht: gewicht['weight'])

for fruit in fruitmand:
    print(fruit['name'], fruit['weight'])