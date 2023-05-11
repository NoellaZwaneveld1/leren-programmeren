from fruitmand import fruitmand

lengte_fruitnaam = 0

for fruitnaam in fruitmand:
    lengte_fruitnaam_check = len(fruitnaam['name'])
    if lengte_fruitnaam_check > lengte_fruitnaam:
        lengte_fruitnaam = lengte_fruitnaam_check	

for fruit in fruitmand:
    if lengte_fruitnaam == len(fruit['name']):
        naam_fruit = fruit['name']
        kleur_fruit = fruit['color']
        gewicht_fruit = fruit['weight']
        break

gewicht_fruit /= 1000

kleuren_fruit = {
    'yellow' : 'geele',
    'green' : 'groene',
    'orange' : 'oranje',
    'red' : 'roode',
    'brown' : 'bruine'
}

print(f"De {naam_fruit} ({lengte_fruitnaam} letters) heeft een {kleuren_fruit[kleur_fruit]} kleur en een gewicht van {gewicht_fruit}KG")