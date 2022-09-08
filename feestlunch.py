aantalCroissantjes = 17
prijsPerCroissantje = 0.39
croissantjes = aantalCroissantjes * prijsPerCroissantje

aantalStokbroden = 2
prijsPerStokbroden = 2.78
stokbroden = aantalStokbroden * prijsPerStokbroden

aantalKortingsbonnen = 3
kortingPerBon = 0.50
kortingsbonnen = aantalKortingsbonnen * kortingPerBon

totaalPrijs = croissantjes + stokbroden - kortingsbonnen

print('De feestlunch kost je bij de bakker', totaalPrijs, 'voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')