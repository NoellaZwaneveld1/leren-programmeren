aantalCroissantjes = int(input('Hoeveel croissantjes wilt u kopen? '))
prijsPerCroissantje = 0.39
prijsPerCroissantje = prijsPerCroissantje * 100
croissantjes = aantalCroissantjes * prijsPerCroissantje

aantalStokbroden = int(input('Hoeveel stokbroden wilt u kopen? '))
prijsPerStokbrood = 2.78
prijsPerStokbrood = prijsPerStokbrood * 100
stokbroden = aantalStokbroden * prijsPerStokbrood

zonderKorting = croissantjes + stokbroden

aantalKortingsbonnen = int(input('Hoeveel kortingsbonnen heeft u? '))
kortingPerBon = 0.50
kortingPerBon = kortingPerBon * 100 
korting = aantalKortingsbonnen * kortingPerBon

totaal = round( croissantjes * stokbroden - korting)

print (f'De feestlunch kost je bij de bakker {totaal} cent voor de {aantalCroissantjes} croissantjes en de {aantalStokbroden} stokbroden als de {aantalKortingsbonnen} kortingsbonnen nog geldig zijn!')


print('Dit is uw factuur ')

print(f""" 
----------------------------------------------------------------------
Croissantjes :                   € {croissantjes},-
stokbroden   :                   € {stokbroden},-
                                _______________________ +
                                 €{zonderKorting}
                                 €{korting}
                                _______________________ -
                                 €{totaal}
----------------------------------------------------------------------
""")