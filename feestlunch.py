aantalCroissantjes = int(input('Hoeveel croissantjes wilt u kopen? ')) #17 croissantjes
prijsPerCroissantje = float(input('Wat is de prijs per croissantje? ')) #0.39 
prijsPerCroissantje = prijsPerCroissantje * 100
croissantjes = aantalCroissantjes * prijsPerCroissantje

aantalStokbroden = int(input('Hoeveel stokbroden wilt u kopen? ')) #2 stokbroden
prijsPerStokbroden = float(input('Wat is de prijs per stokbrood?')) #2.78
prijsPerStokbroden = prijsPerStokbroden * 100
stokbroden = aantalStokbroden * prijsPerStokbroden

aantalKortingsbonnen = int(input('Hoeveel kortingsbonnen heeft u?')) #3
kortingPerBon = float(input('Hoeveel korting per kortingsbon? ')) #0.50
kortingPerBon = kortingPerBon *100
kortingsbonnen = aantalKortingsbonnen * kortingPerBon

totaalPrijs = croissantjes + stokbroden - kortingsbonnen

print('De feestlunch kost je bij de bakker', totaalPrijs, ' cent voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig')