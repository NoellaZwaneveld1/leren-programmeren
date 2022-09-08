toegangsticketPerPersoon = 7.45
aantalPersonen = 3
toegangTotaal = toegangsticketPerPersoon * aantalPersonen

vipSeatTijd = 45 / 5
vipSeatPrijs = 0.37 
vipseatPerPersoon = vipSeatTijd * vipSeatPrijs
vipseatTotaal = vipseatPerPersoon * aantalPersonen

totaalPrijs = toegangTotaal + vipseatTotaal 

print(totaalPrijs)