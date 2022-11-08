import random

ronde = 0
punten = 0

while ronde < 20:
    getal = random.randint(0, 1000)
    print("""Dit programma kiest een random getal tussen de 0 en 1000. Probeer dit getal te raden, je hebt 5 pogingen.
    """)
    poging = 10
    while poging > 0:
        keuze = int(input("Welk getal kies je? "))
        verschil = abs(getal - keuze)
        if keuze == getal:
            print("Gefeliciteerd! je hebt het getal correct geraden!")
            punten +=1
            break
        if verschil <= 20:
            print("Je bent heel warm")
        elif verschil <= 50:
            print("Je bent warm.")
        poging-=1
    print(punten)
    ronde +=1
    print(f"Ronde: {ronde}")
    if ronde == 10:
        ronde10 = input("U heeft nu 10 rondes gehad. Wilt u nog verder?")
        if ronde10 == "nee":
            exit()
    elif ronde == 20:
        print(f"Je heb nu 20 rondes gespeeld. je totale score is: {punten}.")
    

