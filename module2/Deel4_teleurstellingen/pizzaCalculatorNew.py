small_prijs = 9.99
medium_prijs = 10.99
large_prijs = 14.50

size = 0 

while size == 0:
    try:
        small_aantal = int(input("Hoeveel small pizza's wilt u? "))
        size+=1

    except:
        print("Vul een heel getal in ")

while size == 1:
    try:
        medium_aantal = int(input("Hoeveel medium pizza's wilt u? "))
        size+=1

    except:
        print("Vul een heel getal in ")

while size == 2:
    try:
        large_aantal = int(input("Hoeveel large pizza's wilt u? "))
        size+=1

    except: 
        print("Vul een heel getal in ")

totaal_small = round(small_prijs * small_aantal, 2)
totaal_medium = round(medium_prijs * medium_aantal, 2)
totaal_large = round(large_prijs * large_aantal, 2)

totaal_prijs = totaal_small + totaal_medium + totaal_large

print(f"""
Dit is uw bestelling:
--------------------------------------------------------------------------------
Small pizza's:  {small_aantal}x {small_prijs}               = {totaal_small}
Medium pizza's: {medium_aantal}x {medium_prijs}             = {totaal_medium}
Large pizza's: {large_aantal} X {large_prijs}               = {totaal_large}
-------------------------------------------------------------------------------- +
                                                            {totaal_prijs}
 """)