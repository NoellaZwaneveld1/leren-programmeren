from fruitmand import fruitmand

# fruitmand.remove({
#     'name' : 'druif',
#     'weight' : 5,
#     'color' : 'red',
#     'round' : True
# })

# for fruit in fruitmand:
#     print(fruit['color'])

druif_positie = None

for position in range(0, len(fruitmand)):
    # print(fruitmand[position]['name'])
    if fruitmand[position]['name'] == 'druif':
        druif_positie = position

if druif_positie != None:
    fruitmand.pop(druif_positie)

for fruit in fruitmand:
    print(fruit)