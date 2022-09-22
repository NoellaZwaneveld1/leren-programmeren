iphonePrijs = int(input('Hoe duur is de Iphone in euros?'))

samsungPrijs = int(input('Hoe duur is de Samsung in euros?'))

if iphonePrijs > 900 and samsungPrijs > 900:
    
    if iphonePrijs > samsungPrijs:
        print(f""" 
            De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro
            De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro

            Het advies is dus geen telefoon te kopen, ze zijn te duur.
            """)
    else: 
        print(f""" 
            De Iphone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro
            De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

            Het advies is dus geen telefoon te kopen, ze zijn te duur.
            """) 

elif iphonePrijs > 900:
     print(f""" 
            De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro
            De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro

            Het advies is dus de samsung te kopen, de Iphone is namelijk te duur.
            """)
elif samsungPrijs > 900:
     print(f""" 
            De Iphone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro
            De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

            Het advies is dus de Iphone te kopen, de Samsung is namelijk te duur.
            """)

else:
    if iphonePrijs > samsungPrijs:
        print(f""" 
        De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro
        De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro
        """)

        verschil = iphonePrijs - samsungPrijs

        if verschil <= 50:
            print(f'Het advies is dus de Iphone te kopen. Deze is namelijk maar {verschil} euro duurder dan de Samsung')
        
        else:
            print(f'Het advies is dus de Samsung te kopen. Deze is namelijk {verschil} euro goedkoper dan de iphone')

    elif iphonePrijs < samsungPrijs:
        verschil = samsungPrijs - iphonePrijs
        print(f"""
            De Iphone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro
            De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

            Het advies is dus de Iphone te kopen. Deze is namelijk {verschil} euro goedkoper.
            """)

    else:
        print(f""" 
        Beide telefoons zijn even duur, ze kosten allebei {iphonePrijs}

        Het advies is dus de Iphone te kopen, aangezien ze allebei even duur zijn.
        """)