aantal_croissantjes = int(input("Hoeveel croissantjes wilt u kopen? "))#17
prijs_croissantjes = float(input("Wat is de prijs per croissantje? "))#0.39
prijs_croissantjes = prijs_croissantjes *100
croissantjes = prijs_croissantjes * aantal_croissantjes

aantal_stokbroden = int(input("Hoeveel stokbroden wilt u kopen? ")) #2
prijs_stokbroden = float(input("Wat is de prijs per stokbrood? ")) #2.78
prijs_stokbroden = prijs_stokbroden *100
stokbroden = prijs_stokbroden * aantal_stokbroden

aantal_kortingsbonnen = int(input("Hoeveel kortingsbonnen heeft u? ")) #3
korting_per_bon = float(input("Hoeveel kortinhg krijgt u per bon? ")) #0.50
korting_per_bon = korting_per_bon *100
korting = korting_per_bon *aantal_kortingsbonnen

totaal = croissantjes + stokbroden - korting

print(f"De feestlunch kost je bij de bakker {totaal} cent voor de {aantal_croissantjes} croissantjes en de {aantal_stokbroden} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig")