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

if kleur_fruit == 'yellow':
    kleur_fruit = 'geele'
if kleur_fruit == 'green':
    kleur_fruit = 'groene'
if kleur_fruit == 'orange':
    kleur_fruit = 'oranje'
if kleur_fruit == 'red':
    kleur_fruit = 'roode'
if kleur_fruit == 'brown':
    kleur_fruit = 'bruine'

print(f"De {naam_fruit} ({lengte_fruitnaam} letters) heeft een {kleur_fruit} kleur en een gewicht van {gewicht_fruit}KG")