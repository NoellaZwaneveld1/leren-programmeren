print("""
Er wordt u een aantal vragen gesteld die relevant zijn aan de solicitatie voor 'Circusdirecteur voor Circus HotelDeBotel'
Gelieve deze vragen eerlijk en serieus in te vullen.
Als blijkt dat u aan de criteria voldoet dan komt u in aanmerking voor een solicitatie gesprek!
Hier komen de vragen, veel succes!!!
""")

vraag1_ervaring = input("""Heeft u praktijk ervraring in 1 van deze beroepen? zo ja, waar heeft u ervaring in?
- dieren-dresuur
- jongleren
- acrobatiek
""")

score = 0 

if vraag1_ervaring == 'nee': 
    score = score + 0

if vraag1_ervaring == 'dieren-dresuur':
    print ('Hoeveel jaar praktijk ervaring heeft u in dieren-dresuur? ')

    ervaringDresuur = input()

    if int(ervaringDresuur) <= 4:
         score = score + 0         

    elif int(ervaringDresuur) > 4:
         score = score + 1


if vraag1_ervaring == 'jongleren':
    print ('Hoeveel jaar praktijk ervaring heeft u in jongleren? ')

    ervaringJongleren = input()

    if int(ervaringJongleren) <= 5:
         score = score + 0

    elif int(ervaringJongleren) > 5: 
         score = score + 1


if vraag1_ervaring == 'acrobatiek':
    print ('Hoeveel jaar praktijk ervaring heeft u in acrobatiek? ')

    ervaringAcrobatiek = input()

    if int(ervaringAcrobatiek) <= 3:
         score = score + 0

    elif int(ervaringAcrobatiek) > 3:
         score = score + 1


vraag2_diploma = input('Heeft u een MBO diploma in ondernemen? ')

if vraag2_diploma == 'ja':
     print('Welk niveau diploma heeft u? ')

     vraag3_niveau = input()

     if int(vraag3_niveau) < 4:
         score = score + 0

     elif int(vraag3_niveau	) == 4:
         score = score + 1

elif vraag2_diploma == 'nee':
     score = score + 0

vraag3_vrachtwagen = input('Heeft u een geldig vrachtwagen rijbewijs? ')

if vraag3_vrachtwagen == 'ja':
     score = score + 1

elif vraag3_vrachtwagen == 'nee':
     score = score + 0

vraag4_hoed = input('Heeft u een hoge hoed? ')

if vraag4_hoed == 'ja':
     score = score + 1

elif vraag4_hoed == 'nee':
     score = score + 0

vraag5_manOfVrouw = input('Bent u een man of een vrouw? ')

if vraag5_manOfVrouw == 'man': 
     print('Heeft u een snor' )

     vraag6_snor = input()
     
     if vraag6_snor == 'nee':
         score = score + 0

     elif vraag6_snor == 'ja':
         score = score + 1

     vraag7_breedte = input('Hoe breedt is uw snor in centimeters? ')

     if int(vraag7_breedte) <= 10:
         score = score + 0
    
     elif int(vraag7_breedte) > 10:
         score = score + 1

if vraag5_manOfVrouw == 'vrouw':
     print('Heeft u rood krulhaar? ')

     vraag6_krulhaar = input()

     if vraag6_krulhaar == 'ja':
         score = score + 1

         vraag7_lengte = input('Hoe lang is uw haar in centimeters? ')

         if int(vraag7_lengte) <= 20:
             score = score + 0
        
         elif int(vraag7_lengte) > 20:
             score = score + 1


     elif vraag6_krulhaar == 'nee':
         score = score + 0

vraag8_lengte = input('Hoelang bent u in centimeters? ')

if int(vraag8_lengte) <= 150:
     score = score + 0

elif int(vraag8_lengte) > 150:
     score = score + 1

vraag9_gewicht = input('Hoe zwaar bent u in kg? ')

if int(vraag9_gewicht) <= 90:
     score = score + 0

elif int(vraag9_gewicht) > 90:
     score = score + 1

vraag10_certificaat = input('Heeft u een certificaat "overleven met gevaarlijk personeel"? ')

if vraag10_certificaat == 'ja':
     score = score + 1

elif vraag10_certificaat == 'nee':
     score = score + 0


if score < 9:
     print('Helaas, u bent niet geschikt voor deze positie')
     exit() 

if score == 9:
    print('Gefeliciteerd, u komt in aanmerking voor een solicitatie gesprek. Stuur snel uw cv!')
    exit()