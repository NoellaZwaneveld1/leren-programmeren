
print('Beantwoord de vragen met ja of nee ')

vraag1_kleur = input('Is de kaas geel? ')
 
if vraag1_kleur == "nee":
    print('Heeft de kaas blauwe schimmel? ')

    vraag2_schimmel = input()

    if vraag2_schimmel == 'nee':
        print('Mozarella')
    elif vraag2_schimmel == 'ja':
        print('Heeft de kaas een korst?')

        vraag4_korst = input()

        if vraag4_korst == 'nee':
            print('Foume d Ambert')
        elif vraag4_korst == 'ja':
            print('Blue de Rochbaron')

elif vraag1_kleur == 'ja':
    print('Zitten er gaten in de kaas? ')

    vraag3_gaten = input()

    if vraag3_gaten == 'nee':
        print('Is de kaas hard als steen? ')

        vraag5_steen = input()

        if vraag5_steen == 'nee':
            print('Goudse kaas')
        elif vraag5_steen == 'ja':
            print('Parmigiano Reggiano')

    elif vraag3_gaten == 'ja':
        print('Is de kaas belachelijk duur? ')

        vraag6_duur = input()
        
        if vraag6_duur == 'nee':
            print('Leerdammer')
        elif vraag6_duur == 'ja':
            print('Emmenthaler')
