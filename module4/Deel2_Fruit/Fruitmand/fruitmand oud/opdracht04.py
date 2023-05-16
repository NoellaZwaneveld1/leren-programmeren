from fruitmand import fruitmand
import random

getal = int(input("Vul een getal in "))

for aantalFruit in range(0, getal):
    randomFruit = random.choice(fruitmand)
    print(randomFruit['name'])
    # if randomFruit == randomFruit['name']:
    #     fruitmand.pop(randomFruit)
    