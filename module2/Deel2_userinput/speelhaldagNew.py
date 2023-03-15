prijs_ticket = float(input("Hoeveel kost een ticket per persoon? ")) #7.45
prijs_ticket = prijs_ticket * 100
aantal_personen = int(input("Voor hoeveel personen wil je tickets kopen? ")) #4
toegang = prijs_ticket * aantal_personen

vipseat_tijd = int(input("Hoeveel minuten wil je in de VR-vip seat? ")) #45
vipseat_prijs = float(input("Hoeveel kost de VR-vip seat per 5 minuten? "))#0.37
vipseat_prijs = vipseat_prijs * 100
vipseat_per_persoon = vipseat_tijd / 5 * vipseat_prijs
vipseat = vipseat_per_persoon * aantal_personen

totaal = toegang + vipseat

print(f"Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {vipseat_tijd} minuten VR kost je maar {totaal} cent")