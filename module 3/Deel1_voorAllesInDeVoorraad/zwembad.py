lengte = float(input('Hoelang is het zwembad?' ))
breedte = float(input('Hoe breed is het zwembad? '))
hoogte = float(input('Hoe diep is het Zwembad? '))

inhoudZwembad = round(lengte * breedte * hoogte, 2)

uitgraven = 25
uitgravenPrijs = uitgraven * inhoudZwembad

afvoeren = 32.50 
afvoerenPrijs = afvoeren * inhoudZwembad

voorrijKosten = 250
prijsPerKm = 2.05
aantalKm = 60
PrijsPerKmTotaal = prijsPerKm * aantalKm
voorrijKostenTotaal = round(voorrijKosten + PrijsPerKmTotaal, 2)


totaal = round(uitgravenPrijs + afvoerenPrijs + voorrijKostenTotaal, 2) 

print(f"""Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud: {inhoudZwembad} m3)
Uitgraven:         €{uitgravenPrijs}
Afvoeren grond:    €{afvoerenPrijs}
VoorrijKosten:     €{voorrijKostenTotaal}
Totaal:            €{totaal}
""")