print("""
Er wordt u een aantal vragen gesteld die relevant zijn aan de solicitatie voor 'Circusdirecteur voor Circus HotelDeBotel'
Gelieve deze vragen eerlijk en serieus in te vullen.
Als blijkt dat u aan de criteria voldoet dan komt u in aanmerking voor een solicitatie gesprek!
Hier komen de vragen, veel succes!!!
""")

ervaring= (input('Heeft u praktijk ervaring in Dieren-dresuur, jongleren of acrobatiek? ')) 

if (ervaring == 'ja'): 
     soort_ervaring = int(input("""Waar heeft u ervaring in?
                    1: dieren-dresuur
                    2: jongleren
                    3: acrobatiek
                    """))

     jaren_ervaring = input('Hoeveel jaar praktijk ervaring heeft u daar in? ')

     if ((soort_ervaring == 1) and (int(jaren_ervaring) > 4)) or ((soort_ervaring == 2) and (int(jaren_ervaring) > 5)) or ((soort_ervaring == 3) and (int(jaren_ervaring) > 3)):
      ervaring = True 

vraag2_diploma = input('Heeft u een MBO diploma in ondernemen? ')

if vraag2_diploma == 'j':
     print('Welk niveau diploma heeft u? ')

     vraag3_niveau = input()

     if int(vraag3_niveau) == 4:
         pass

vraag3_vrachtwagen = input('Heeft u een geldig vrachtwagen rijbewijs? ')

if vraag3_vrachtwagen == 'j':
     pass

vraag4_hoed = input('Heeft u een hoge hoed? ')

if vraag4_hoed == 'j':
     pass

vraag5_manOfVrouw = input('Bent u een man of een vrouw? ')

if vraag5_manOfVrouw == 'man': 
     print('Heeft u een snor' )

     vraag6_snor = input()

     if vraag6_snor == 'j':
         pass

     vraag7_breedte = input('Hoe breedt is uw snor in centimeters? ')
    
     if int(vraag7_breedte) > 10:
             pass

if vraag5_manOfVrouw == 'vrouw':
     print('Heeft u rood krulhaar? ')

     vraag6_krulhaar = input()

     if vraag6_krulhaar == 'j':
         pass

         vraag7_lengte = input('Hoe lang is uw haar in centimeters? ')
        
         if int(vraag7_lengte) > 20:
             pass

if ((vraag5_manOfVrouw == 'man') and (vraag6_snor == 'ja') and (vraag7_breedte > 10)) or ((vraag5_manOfVrouw == 'vrouw') and (vraag6_krulhaar == 'ja') and (int(vraag7_lengte) > 20)):
    vraag5_manOfVrouw = True

vraag8_lengte = input('Hoelang bent u in centimeters? ')

if int(vraag8_lengte) > 150:
      pass

vraag9_gewicht = input('Hoe zwaar bent u in kg? ')

if int(vraag9_gewicht) > 90:
     pass

vraag10_certificaat = input('Heeft u een certificaat "overleven met gevaarlijk personeel"? ')

if vraag10_certificaat == 'j':
     pass

if ((ervaring == True) and (vraag2_diploma =='j') and (vraag3_vrachtwagen == 'j') and (vraag4_hoed == 'j') and (vraag5_manOfVrouw == True) and (int(vraag8_lengte) > 150) and (int(vraag9_gewicht) > 90) and (vraag10_certificaat == 'j')):   
     print('Gefeliciteerd, u komt in aanmerking voor een solicitatie gesprek. Stuur snel uw cv!')

else:
     print('Helaas, u bent niet geschikt voor deze positie')
