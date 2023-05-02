from fruitmand import fruitmand

fruitmand.append({
    'name': 'watermeloen',
    'weight': 2500,
    'color' : 'green',
    'round' : True
})

for fruit in fruitmand:
    print(fruit['weight'])