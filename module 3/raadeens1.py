import random

ronde = 0
punten = 0

while ronde < 20:
    getal = random.randint(1, 1000)
    print("""Dit programma kiest een random getal tussen de 0 en 1000. Probeer dit getal te raden, je hebt 10 pogingen.
    """)
    poging = 10 #je krijgt 10 pogingen per ronde
    while poging > 0:
        keuze = int(input("Welk getal kies je? "))
        if keuze <= getal:
            print("Hoger")
        elif keuze >= getal:
            print("Lager")
        
        if keuze == getal:
            print("Gefeliciteerd! je hebt het getal correct geraden!")
            punten +=1 #telt 1 punt op bij de punten
            break #stopt deze while loop
        if abs(getal - keuze) <= 20: #geeft de absolute waarde van het gegeven getal terug
            print("Je bent heel warm")
        elif abs(getal - keuze) <= 50:
            print("Je bent warm.")
        poging-=1
        print(f"Je heb nog {poging} pogingen") #laat zien hoeveel pogingen je nog heb

    print(f"punt(en):{punten}") #geeft aan hoeveel punten je heb
    ronde +=1 #telt een ronde op
    print(f"Ronde: {ronde}") #laat zien hoeveel ronde's je heb gehad

    if ronde == 10: 
        ronde10 = input("U heeft nu 10 rondes gehad. Wilt u nog verder?")#als je 10 rondes heb gehad vraagt het programma of je nog door wil
        if ronde10 == "nee":
            exit()#als je nee zegt dan stopt het programma, anders gaat hij verder
    elif ronde == 20:
        print(f"Je heb nu 20 rondes gespeeld. je totale score is: {punten}.") #laat zien wat je totale score is