import random

deck = []
kleurenKaarten = ("Harten", "Klaveren", "Schoppen", "Ruiten")
nummersKaarten = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas")

for aantalKleuren in range(0, 4): #zorgt dat de 4 kleuren en de 13 nummers per kleur aan het deck wordt toegevoegd
    for aantalKaarten in range(0, 13):
        deck.append(kleurenKaarten[aantalKleuren] + " " + nummersKaarten[aantalKaarten]) #met append voeg je iets toe aan een list

deck.append("joker") #voegt 2 keer een joker toe aan de deck
deck.append("joker")
random.shuffle(deck) #shuffelt het deck

for randomKaart in range(1, 8): #heraalt dit 7 keer
    print(f"kaart {randomKaart}: ", deck[randomKaart])#kiest 1 kaart uit het deck
    deck.pop(randomKaart) #verwijdert de kaart uit de lijst
print("Deck (",len(deck), "kaarten): ", deck) #laat zijn hoeveel kaarten er nog in de deck zitten (len)