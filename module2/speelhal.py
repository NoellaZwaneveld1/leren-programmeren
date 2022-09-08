toegangsticketPerPersoon = float(input('Hoeveel kost een ticket per persoon? ')) #7.45
toegangsticketPerPersoon = toegangsticketPerPersoon * 100 
aantalPersonen = int(input('Met hoeveel personen ben je? '))  #4
toegangTotaal = toegangsticketPerPersoon * aantalPersonen #29.8 euro in totaal

vipSeatTijd = int(input('Hoeveel minuten wil je in de VR-vip seat? '))  #45
vipSeatPrijs = float (input('Wat is de prijs per 5 minuten? '))#0.37 per 5 minuten 
vipSeatPrijs = vipSeatPrijs * 100
vipseatPerPersoon = vipSeatTijd / 5 * vipSeatPrijs
vipseatTotaal = vipseatPerPersoon * aantalPersonen #13.32 in totaal

totaalPrijs = toegangTotaal + vipseatTotaal 

print('Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar', totaalPrijs, 'cent')