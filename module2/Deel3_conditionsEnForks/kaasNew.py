kaas_kleur = input("is de kaas geel? ")

if kaas_kleur == 'j':
    kaas_gaten = input("Zitten er gaten in de kaas? ")

    if kaas_gaten == 'j':
        kaas_prijs = input("Is de kaas belagelijk duur? ")

        if kaas_prijs == 'j':
            print("Kaas: Emmentaler")
        
        elif kaas_prijs == "n":
            print("Kaas: Leerdammer")

    elif kaas_gaten == 'n':
        kaas_steen = input("Is de kaas hard als steen? ")

        if kaas_steen == 'j':
            print("Kaas: Parmigiano Reggiano")
        
        elif kaas_steen == 'n':
            print("Kaas: Goudse Kaas")



elif kaas_kleur == 'n':
    kaas_schimmel = input("heeft de kaas blauwe schimmel? ")

    if kaas_schimmel == 'j':
        kaas_korst = input("Heeft de kaas een korst? ")

        if kaas_korst == 'j':
            print("Kaas: Blue de Rochbaron")
        
        elif kaas_korst == 'n':
            print("Foume d'Ambert")

    if kaas_schimmel == 'n':
        kaas_korst = input("Heeft de kaas een korst? ")

        if kaas_korst == 'j':
            print("Kaas: Camembert")
        
        if kaas_korst == 'n':
            print("Kaas: Mozarella")