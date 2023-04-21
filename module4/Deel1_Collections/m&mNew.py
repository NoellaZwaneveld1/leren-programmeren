import random

kleuren = ('oranje', 'blauw', 'groen', 'bruin')
zakMnM = { }

while True:
    try:
        aantalMnM = int(input("Hoeveel M&M's zitten er in de zak? "))
        break
    except:
        print("Vul een getal in!")

for kleur in kleuren:
    zakMnM[kleur] = 0

for i in range (0, aantalMnM):
    randomKleur = random.randint(0, len(kleuren)-1)
    zakMnM[kleuren[randomKleur]] +=1

for kleur in kleuren:
    if zakMnM[kleur] == 0:
        zakMnM.pop[kleur]#haalt de kleur weg als er 0 m&m's van die kleur in de zak zitten

print(zakMnM)