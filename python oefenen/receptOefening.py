#ingrediënten voor Tzatziki


print('Bereken de ingrediënten')

aantalKomkommers = int(input('Hoeveel komkommers: '))

mespuntperkomkommer = 1
mespuntZeezout = aantalKomkommers * mespuntperkomkommer

knoflookperkomkommer = 2
tenenKnoflook = aantalKomkommers * knoflookperkomkommer

dilleperkomkommer = 15
verseDille = aantalKomkommers * dilleperkomkommer

yoghurtperkomkommer = 500
griekseYoghurt = aantalKomkommers * yoghurtperkomkommer

azijnperkomkommer = 1
wittewijnAzijn = aantalKomkommers * azijnperkomkommer

olieperkomkommer = 3
olijfolie = aantalKomkommers * olieperkomkommer

print(f""" 
Dit zijn de ingrediënten die u nodig heeft voor dit recept:
                  - {mespuntZeezout} mespunten zeezout
                  - {tenenKnoflook} tenen knoflook
                  - {verseDille} gram verse dille
                  - {griekseYoghurt} gram griekse yoghurt
                  - {wittewijnAzijn} eetlepels witte wijn azijn
                  - {olijfolie} eetlepels olijfolie

Dit recept is voor {aantalKomkommers} personen
""")
