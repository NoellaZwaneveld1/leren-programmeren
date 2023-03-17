print("""Vacature: Circusdirecteur voor Circus HotelDeBotel.
    Er worden een aantal vragen gesteld aan u, aan de hand van de antwoorden krijgt u te horen of u geschikt ben voor deze baan en dus verder mag gaan met de solicitatie.
    """)

print("Vraag 1: ")
diploma = int(input("Welk niveau mbo diploma heeft u in ondernemen? ")) #4

print("Vraag 2: ")
vrachtwagen_rijbewijs = input("Heeft u een geldig vrachtwagen rijbewijs? ") #ja

print("Vraag 3: ")
hoge_hoed = input("Bent u in bezit van een hoge hoed? ") #ja

print("Vraag 4: ")
geslacht = input("Bent u een man of een vrouw? ") 

if geslacht == 'man':
    snor = input("Heeft u een snor? ") #ja
    if snor == 'ja':
        snor_breedte = input("Hoe breedt is uw snor in centimeters? ") #groter dan 10cm

elif geslacht == 'vrouw':
    haar_kleur = input("Heeft u rood krulhaar? ") #ja
    if haar_kleur == 'ja':
        haar_lengte = input("Hoelang is uw haar? ") #langer dan 20 cm

if ((geslacht== 'man') and (snor == 'ja' ) and(int(snor_breedte)> 10 )) or ((geslacht == 'vrouw') and (haar_kleur == 'ja') and (int(haar_lengte)> 20 )):
    vraag_4 = True

print("Vraag 5: ")
lengte = int(input("Wat is uw lengte in centimeters? ")) #langer dan 150 en korter dan #220

if ((lengte > 150) and (lengte < 220)):
    lengte = True

print("Vraag 6: ")
gewicht = int(input("Wat is uw gewicht in Kilo's? ")) #zwaarder dan 90kg en lichter dan 120kg

if ((gewicht > 90) and (gewicht < 120)):
    gewicht = True

print("Vraag 7: ")
certificaat = input("Heeft Certificaat 'Overleven met gevaarlijk personeel?' ") #ja

print("Vraag 8: ")
ervaring_dierenDresuur = int(input("Hoeveel jaar praktijk ervaring heeft u in dieren dresuur? ")) #meer dan 4 jaar

print("Vraag 9: ")
ervaring_jongleren = int(input("Hoeveel jaar praktijk ervaring heeft u in jongleren? ")) #meer dan 5 jaar

print("Vraag 10: ")
ervaring_acrobatiek = int(input("Hoeveel jaar praktijk ervaring heeft u in acrobatiek?")) #meer dan 3 jaar

if ((ervaring_dierenDresuur >= 4) or (ervaring_jongleren >= 5) or (ervaring_acrobatiek >= 3)):
    ervaring = True

else: 
    ervaring = False


if ((int(diploma == 4) and (vrachtwagen_rijbewijs == 'ja') and (hoge_hoed == 'ja') and (vraag_4 == True) and (lengte == True) and (gewicht == True) and (certificaat == 'ja') and (ervaring == True))):
    print("Gefeliciteerd, u mag verder met de solicitatie! er wordt spoedig contact opgenomen met u.")

else:
    print("Helaas, u bent niet geschikt voor deze baan")


