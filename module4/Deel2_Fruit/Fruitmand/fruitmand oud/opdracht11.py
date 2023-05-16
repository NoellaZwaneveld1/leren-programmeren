from fruitmand import fruitmand

fruitKleuren = [] #lege list

for kleuren in fruitmand:
    fruitKleuren.append(kleuren['color']) #zet alle kleuren in de lege list

while True:
    welkeKleur = input("Welke kleur is het fruit? ")
    if welkeKleur in fruitKleuren:
        break
    else:
        print("Vul een kleur in die in de fruitmand zit")

rond = 0
niet_rond = 0

for fruit in fruitmand:
    alleKleuren = fruit['color']
    if alleKleuren == welkeKleur:
        if fruit['round']:
            rond+=1
        else:
            niet_rond +=1

verschil = abs(rond - niet_rond)

if rond > niet_rond:
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten van de kleur {welkeKleur}")
if rond < niet_rond:
    print(f"Er zijn {verschil} meer niet ronde vruchten dan ronde vruchten van de kleur {welkeKleur}")
else: 
    print(f"Er zijn evenveel ronde als niet ronde vruchten van de kleur {welkeKleur}")

print(f"rond = {rond}")
print(f"niet rond = {niet_rond}")