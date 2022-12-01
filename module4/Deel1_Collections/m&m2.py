import random

kleuren = ("Oranje", "Blauw", "Groen", "Bruin")
zakMnM = {}

while True: #zorgt dat je een nummer in moet vullen
    try:
        aantalMnM = int( input("Hoeveel m&m's zitten in de zak: "))
        break
    except:
        print("Voer een nummer in aub!")
    
for kleur in kleuren:
    zakMnM[kleur] = 0

for i in range(0, aantalMnM): #van 0 tot het aantal M&M's
    randomkleur = random.randint(0, len(kleuren)-1) #haalt een kleur weg
    zakMnM[kleuren[randomkleur]] +=1 

for kleur in kleuren:
    if zakMnM[kleur] == 0:
        zakMnM.pop[kleur]#haalt de kleur weg als er 0 m&m's van die kleur in de zak zitten

print(zakMnM)