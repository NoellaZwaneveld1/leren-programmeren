#ingrediënten voor Tzatziki


print('Bereken de ingrediënten')

aantalKomkommers = input('Hoeveel komkommers: ')
aantalKomkommers = int(aantalKomkommers)

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

print('Hoeveel mespuntjes zeezout heb je nodig:', mespuntZeezout)
print('Hoeveel tenen knoflook heb je nodig:', tenenKnoflook)
print('Hoeveel gram verse dille heb je nodig:', verseDille)
print('Hoeveel gram griekse yoghurt heb je nodig:', griekseYoghurt)
print('Hoeveel eetlepels witte wijn azijn heb je nodig:', wittewijnAzijn)
print('Hoeveel eetlepels olijfolie heb je nodig:', olijfolie)