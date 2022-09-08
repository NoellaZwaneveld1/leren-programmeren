toegangsticketPerPersoon = 7.45
aantalPersonen = 4
toegangTotaal = toegangsticketPerPersoon * aantalPersonen

vipSeatTijd = 45 / 5
vipSeatPrijs = 0.37 
vipseatPerPersoon = vipSeatTijd * vipSeatPrijs
vipseatTotaal = vipseatPerPersoon * aantalPersonen

totaalPrijs = toegangTotaal + vipseatTotaal 

print('Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar', totaalPrijs, 'euro')