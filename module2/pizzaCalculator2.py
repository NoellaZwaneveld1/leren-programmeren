small = 9.94
medium = 10.99
large = 14.49

var = 0

while var == 0:
    try:
        smallPizzas = int(input("Hoeveel small pizza's wilt u? "))  
        var +=1
    except:
        print('Vul een heel getal in')

while var == 1:
    try:
        mediumPizzas = int(input("Hoeveel medium pizza's wilt u? "))
        var +=1
    except:
        print('Vul een heel getal in')

while var == 2:
    try: 
        largePizzas = int(input("Hoeveel large pizza's wilt u? "))
        var +=1
    except: 
        print('Vul een heel getal in')

totaalSmall = round(small * smallPizzas, 2)
totaalMedium = round(medium * mediumPizzas, 2)
totaalLarge = round(large * largePizzas, 2) 

totaal = totaalSmall + totaalMedium + totaalLarge

print(f"U heeft {smallPizzas} small pizza's, {mediumPizzas} medium pizza's en {largePizzas} large pizza's")
print(f"""
------------------------------------------------------------
                            BON
|Small pizza's:  {smallPizzas}  x {small}  = {totaalSmall} 
|Medium pizza's: {mediumPizzas} x {medium} = {totaalMedium}
|Large pizza's:  {largePizzas}  x {large}  = {totaalLarge} 
------------------------------------------------------------
""")
     