small_prijs = 10.99
medium_prijs = 12.50
large_prijs = 15.99

small_pizzas = int(input("Hoeveel small pizza's wilt u? "))
medium_pizzas = int(input("Hoeveel medium pizza's wilt u? "))
large_pizzas = int(input("Hoeveel large pizza's wilt u?"))

small_totaal = small_prijs * small_pizzas
medium_totaal = medium_prijs * medium_pizzas
large_totaal = large_prijs * large_pizzas

uitgave = round(small_totaal + medium_totaal + large_totaal, 2)

print(f"""Uw bestelling:
    -------------------------------------------------------------- 
    small pizza's  = {small_pizzas}  X             {small_totaal}
    medium pizza's = {medium_pizzas}  X             {medium_totaal}
    large pizza's  = {large_pizzas}  X             {large_totaal}
    --------------------------------------------------------------
                        TOTAAL:                    {uitgave}
    """)