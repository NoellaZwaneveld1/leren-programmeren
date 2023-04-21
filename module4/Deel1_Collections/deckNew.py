import random # zorgt dat de random functie werkt

deck = [ ] #hier komen alle kaarten in te staan
kleuren_kaarten = ( "Harten", "Klaveren", "Schoppen", "Ruiten") #de kleuren van de kaarten
nummers_kaarten = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas") #de kaarten die in de deck moeten

for aantalKleuren in range(0,4): #zorgt dat alle 4 de kleuren in het deck komen
    for aantalKaarten in range(0, 13): #zorgt dat alle 13 kaarten van de 4 kleuren in het deck komen
        deck.append(kleuren_kaarten[aantalKleuren] + " " + nummers_kaarten[aantalKaarten]) #append voegt iets toe aan het deck. hij voegt alle kleuren en nummers toe aan het deck

deck.append("Joker")
deck.append("Joker")#voegt twee keer een joker toe aan het deck
random.shuffle(deck)#Shuffelt het deck

for randomKaart in range(1, 8): #herhaalt deze loop 7 keer
    print(f"Kaart {randomKaart}: ", deck[randomKaart])#print het kaart nummer + de random kaart die het programma uit heeft gekozen
    deck.pop(randomKaart) #verwijdert de random kaart van de deck
print("Deck (", len(deck), "kaarten: ", deck) #print hoeveel kaarten er in het deck zitten


