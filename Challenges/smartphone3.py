iphonePrijs = int(input('Hoe duur is de Iphone in euros?'))
samsungPrijs = int(input('Hoe duur is de Samsung in euros?'))
asusPrijs = int(input('Hoe duur is de Asus?'))

iphone = 'Iphone'
Samsung = 'Samsung'
Asus = 'Asus'

if ((iphonePrijs > samsungPrijs) and (samsungPrijs > asusPrijs)):
    goedkoopste = 'Asus'
    goedkoopstePrijs = asusPrijs
    tussenIn = 'Samsung'
    tussenInPrijs = samsungPrijs
    duurste = 'Iphone'
    duurstePrijs = iphonePrijs

elif ((iphonePrijs > samsungPrijs) and (samsungPrijs < asusPrijs)):
    goedkoopste = 'Samsung'
    goedkoopstePrijs = samsungPrijs
    tussenIn = 'Asus'
    tussenInPrijs = samsungPrijs
    duurste = 'Iphone'
    duurstePrijs = iphonePrijs

elif ((iphonePrijs < samsungPrijs) and (iphonePrijs > asusPrijs)):
    goedkoopste = 'Asus'
    goedkoopstePrijs = asusPrijs
    tussenIn = 'Iphone'
    tussenInPrijs = iphonePrijs
    duurste = 'Samsung'
    duurstePrijs = samsungPrijs

elif ((iphonePrijs < samsungPrijs) and (iphonePrijs < asusPrijs)):
    goedkoopste = 'Iphone'
    goedkoopstePrijs = iphonePrijs
    tussenIn = 'Asus'
    tussenInPrijs = asusPrijs
    duurste = 'Samsung'
    duurstePrijs = samsungPrijs

elif ((asusPrijs > iphonePrijs) and (iphonePrijs > samsungPrijs)):
    goedkoopste = 'Samsung'
    goedkoopstePrijs = samsungPrijs
    tussenIn = 'Iphone'
    tussenInPrijs = iphonePrijs
    duurste = 'Asus'
    duurstePrijs = asusPrijs

elif ((asusPrijs > iphonePrijs) and (iphonePrijs < samsungPrijs)):
    goedkoopste = 'Iphone'
    goedkoopstePrijs = iphonePrijs
    tussenIn = 'Samsung'
    tussenInPrijs = samsungPrijs
    duurste = 'Asus'
    duurstePrijs = asusPrijs

verschil1 = int(tussenInPrijs - goedkoopstePrijs)
verschil2 = int(duurstePrijs - goedkoopstePrijs)
verschil3 = iphonePrijs - samsungPrijs
verschil4 = iphonePrijs - asusPrijs
verschil5 = samsungPrijs - asusPrijs

print(f""" 
        De {goedkoopste} is het goedkoopst, de telefoon kost: {goedkoopstePrijs} Euro
        De {tussenIn} zit daar tussenin met: {tussenInPrijs} Euro
        De {duurste} is het duurst, de telefoon kost: {duurstePrijs} Euro
        
        De {goedkoopste} schilt {verschil1} met de {tussenIn} en {verschil2} met de {duurste}
        """)

if ((duurstePrijs > 900) and (tussenInPrijs > 900) and (goedkoopstePrijs > 900)):
    print('Het advies is om geen telefoon te kopen, ze zijn te duur.')

elif ((duurstePrijs> 900) and (tussenInPrijs > 900)):
        print(f'Het advies is dus om de {goedkoopste} te kopen')

elif ((duurstePrijs> 900) and (tussenInPrijs < 900)):
    if (( goedkoopste == 'Asus') and (verschil4 >= 100) and (verschil5 >= 100)):
        print('Het advies is dus om de Asus te kopen')
    
    elif ((goedkoopste == 'Iphone') and (verschil3 <= 50)):
        print('Het advies is dus om de Iphone te kopen')
    
    else:
        print('Het advies is dus om de Samsung te kopen')

else:
    if  verschil3 <= 50:
        print('Het advies is dus om de Iphone te kopen')
    
    elif ((verschil4 >= 100) and (verschil5 >= 100)):
        print('Het advies is dus om de Asus te kopen')

    else:
        print('Het advies is om de Samsung te kopen')

