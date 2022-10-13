iphonePrijs = int(input('Hoe duur is de Iphone in euros?'))

samsungPrijs = int(input('Hoe duur is de Samsung in euros?'))

asusPrijs = int(input('Hoe duur is de Asus?'))

verschilIphoneAsus = iphonePrijs - asusPrijs
verschilSamsungAsus = samsungPrijs - asusPrijs

if iphonePrijs > 900 and samsungPrijs > 900 and asusPrijs > 900:
        
    if iphonePrijs > samsungPrijs:
        if asusPrijs < iphonePrijs and  asusPrijs < samsungPrijs:
            print(f""" 
                De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
                De Samsung zit daar tussenin met: {samsungPrijs} Euro
                De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro

                Het advies is dus geen telefoon te kopen, ze zijn te duur.
                """)

        elif asusPrijs < iphonePrijs and  asusPrijs > samsungPrijs:
            print(f""" 
                De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
                De Samsung zit daar tussenin met: {samsungPrijs} Euro
                De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro

                Het advies is dus geen telefoon te kopen, ze zijn te duur.
                """)

        else:
            print(f""" 
                De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro
                De Iphone zit daar tussenin met: {iphonePrijs} Euro
                De Asus is het duurst, de telefoon kost: {asusPrijs} Euro

                Het advies is dus geen telefoon te kopen, ze zijn te duur.
                """)

    else: 
        if asusPrijs < samsungPrijs and asusPrijs < iphonePrijs:
            print(f""" 
                De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
                De Iphone zit daar tussenin met: {iphonePrijs} Euro
                De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

                Het advies is dus geen telefoon te kopen, ze zijn te duur.
                """) 
        
        elif asusPrijs < samsungPrijs and asusPrijs > iphonePrijs:
            print(f""" 
                De Iphone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro
                De Asus zit daar tussenin met: {asusPrijs} Euro
                De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

                Het advies is dus geen telefoon te kopen, ze zijn te duur.
                """)
        else:
            print(f""" 
                De Iphone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro
                De Samsung zit daar tussenin met: {samsungPrijs} Euro
                De Asus is het duurst, de telefoon kost: {asusPrijs} Euro

                Het advies is dus geen telefoon te kopen, ze zijn te duur.
                """)

elif iphonePrijs > 900:
    verschilIphoneSamsung = iphonePrijs - samsungPrijs
    if asusPrijs < iphonePrijs and  asusPrijs < samsungPrijs:
        print(f""" 
            De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
            De Samsung zit daar tussenin met: {samsungPrijs} Euro
            De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro
            """)

        if verschilSamsungAsus < 100:
            print(f"""
            Het advies is dus de Asus te kopen. Deze is namelijk {verschilIphoneAsus} euro goedkoper dan de Iphone
            en {verschilSamsungAsus} euro goedkoper dan de Samsung.
            """)

        else:
            print(f"""
            Het advies is dus de Samsung te kopen. Deze is namelijk {verschilIphoneSamsung} euro goedkoper dan de Iphone
            en {verschilSamsungAsus} euro duurder dan de Asus.
            """)

    elif asusPrijs < iphonePrijs and asusPrijs > samsungPrijs:
        print(f""" 
            De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro
            De Asus zit daar tussenin met: {asusPrijs} Euro
            De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro

            Het advies is dus de Samsung te kopen. Deze is namelijk {verschilIphoneSamsung} euro goedkoper dan de Iphone
            en {verschilSamsungAsus} euro goedkoper dan de Asus.
            """)
    else:
        print(f""" 
                De Iphone is het goedkoopst, de telefoon kost: {samsungPrijs} Euro
                De Samsung zit daar tussenin met: {samsungPrijs} Euro
                De Asus is het duurst, de telefoon kost: {asusPrijs} Euro

                Het advies is dus de Samsung te kopen. Deze is namelijk {verschilIphoneSamsung} euro goedkoper dan de Iphone
                en {verschilSamsungAsus} euro goedkoper dan de Asus.
                """)

elif samsungPrijs > 900:
    verschilSamsungIphone = samsungPrijs - iphonePrijs:

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