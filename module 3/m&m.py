import random

kleur = ("Oranje", "Blauw", "Groen", "Bruin")
zakM = []

hoeveelM = int(input("Hoeveel m&m's zitten er in de zak? "))

while hoeveelM > 0:
    zakM += random.choices(kleur) 
    hoeveelM-=1 
print (f"Dit zijn de m&m's die in de zak zitten: {zakM}")