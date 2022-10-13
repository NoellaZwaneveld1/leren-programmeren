lengte = 8
breedte = 3
hoogte = 1.5

inhoudZwembad = round(lengte * breedte * hoogte, 2)

uitgraven = 25
uitgravenPrijs = uitgraven * inhoudZwembad

afvoeren = 32.50 
afvoerenPrijs = afvoeren * inhoudZwembad

totaal = round(uitgravenPrijs + afvoerenPrijs, 2) 

print(f"""Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud: {inhoudZwembad} m3)
Uitgraven:         €{uitgravenPrijs}
Afvoeren grond:    €{afvoerenPrijs}
Totaal:            €{totaal}
""")