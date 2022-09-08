small = int(input('Hoeveel small pizzas wilt u?' ))
totaalSmall = small * 9.94

medium = int(input('Hoeveel medium pizzas wilt u? '))
totaalMedium = medium * 10.99

large = int(input('Hoeveel large pizzas wilt u?'))
totaalLarge = large * 14.49

totaalPrijs = totaalSmall + totaalMedium + totaalLarge

print(f""" Dit is uw bestelling:

U heeft {small} small pizza's besteld, dit kost {totaalSmall} euro's
U heeft {medium} medium pizza's besteld, dit kost {totaalMedium} euro's
U heeft {large} Large pizza's besteld, dit kost {totaalLarge} euro's

""")
print (f"""
De totaal prijs is {totaalPrijs} euro's

Dit is uw factuur:
-------------------------------------------------------------
Small pizza's:   {small}  x =              €{totaalSmall}
Medium pizza's:  {medium}  x =             €{totaalMedium}
Large pizza's:   {large}  x =              €{totaalLarge}
                                        ____________________ +
                                           €{totaalPrijs}
-------------------------------------------------------------

""")

