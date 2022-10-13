lengte = float(input('Hoelang is het zwembad?' ))
breedte = float(input('Hoe breed is het zwembad? '))
hoogte = float(input('Hoe diep is het Zwembad? '))

inhoudZwembad = round(lengte * breedte * hoogte, 2)
oppervlakteZwembad = round(lengte * breedte, 2)

uitgravenPrijs = 25 * inhoudZwembad
afvoerenPrijs = 32.50 * inhoudZwembad
PrijsPerKmTotaal = round(2.05 * 60, 2)
voorrijKostenTotaal = round(250 + PrijsPerKmTotaal, 2)

if inhoudZwembad < 20:
    betonPrijs = 250

else:
    betonPrijs = 200

betonPrijsTotaal = round(betonPrijs * inhoudZwembad, 2)

totaal = round(uitgravenPrijs + afvoerenPrijs + voorrijKostenTotaal + betonPrijsTotaal, 2) 

print(f"""Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud: {inhoudZwembad} m3)
Uitgraven:                   €{uitgravenPrijs}
Afvoeren grond:              €{afvoerenPrijs}
VoorrijKosten:               €{voorrijKostenTotaal}
beton + tegel ({oppervlakteZwembad} m2):     €{betonPrijsTotaal}
Totaal:                      €{totaal}
""")