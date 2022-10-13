iphonePrijs = int(input('Hoe duur is de Iphone in euros?'))
samsungPrijs = int(input('Hoe duur is de Samsung in euros?'))
asusPrijs = int(input('Hoe duur is de Asus?'))

verschilIphoneAsus = iphonePrijs - asusPrijs #gebruiken als de iphone duurder is
verschilAsusIphone = asusPrijs - iphonePrijs #gebruiken als de asus duurder is

verschilSamsungAsus = samsungPrijs - asusPrijs #gebruiken als de Samsung duurder is
verschilAsusSamsung = asusPrijs - samsungPrijs #gebruiken als de Asus duurder is

verschilIphoneSamsung = iphonePrijs - samsungPrijs #gebruiken als de Iphone duurder is
verschilSamsungIphone = samsungPrijs - iphonePrijs # gebruiken als de Samsung duurder is

if iphonePrijs > 900 and samsungPrijs > 900 and asusPrijs > 900:
        if iphonePrijs > samsungPrijs and samsungPrijs > asusPrijs:
            print(f""" 
                    De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
                    De Samsung zit daar tussenin met: {samsungPrijs} Euro
                    De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro

                    Het advies is dus geen telefoon te kopen, ze zijn te duur.
                    """)
        elif iphonePrijs < samsungPrijs and iphonePrijs > asusPrijs:
            print(f""" 
                De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
                De Iphone zit daar tussenin met: {iphonePrijs} Euro
                De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

                Het advies is dus geen telefoon te kopen, ze zijn te duur.
                """)

elif iphonePrijs > 900 and samsungPrijs < 900 and asusPrijs < 900:
    if ((asusPrijs < samsungPrijs) and (verschilSamsungAsus < 100)):
        print(f""" 
            De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
            De Samsung zit daar tussenin met: {samsungPrijs} Euro
            De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro

            Het advies is dus de Asus te kopen. Deze is namelijk {verschilIphoneAsus} euro goedkoper dan de Iphone
            en {verschilSamsungAsus} euro goedkoper dan de Samsung.
            """)

    elif asusPrijs > samsungPrijs and verschilSamsungAsus > 100:
        print(f""" 
            De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro
            De Asus zit daar tussenin met: {asusPrijs} Euro
            De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro

            Het advies is dus de Samsung te kopen. Deze is namelijk {verschilIphoneSamsung} euro goedkoper dan de Iphone
            en {verschilSamsungAsus} euro goedkoper dan de Asus.
            """)

elif samsungPrijs > 900 and iphonePrijs < 900 and asusPrijs < 900:
    if asusPrijs < iphonePrijs and verschilIphoneAsus < 100:
         print(f""" 
            De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
            De Iphone zit daar tussenin met: {iphonePrijs} Euro
            De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

            Het advies is dus de Asus te kopen. Deze is namelijk {verschilIphoneAsus} euro goedkoper dan de Iphone
            en {verschilSamsungAsus} euro goedkoper dan de Samsung.
            """)
    else:
        print(f""" 
        De iphone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro
        De Asus zit daar tussenin met: {asusPrijs} Euro
        De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

        Het advies is dus de Iphone te kopen. Deze is namelijk {verschilSamsungIphone} euro goedkoper dan de Samsung
        en {verschilAsusIphone} euro goedkoper dan de Asus.
        """)

elif asusPrijs > 900 and iphonePrijs < 900 and samsungPrijs <900:
    if iphonePrijs < samsungPrijs:
         print(f""" 
            De Iphone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro
            De Samsung zit daar tussenin met: {samsungPrijs} Euro
            De Asus is het duurst, de telefoon kost: {asusPrijs} Euro

            Het advies is dus de Iphone te kopen. Deze is namelijk {verschilAsusIphone} euro goedkoper dan de Asus
            en {verschilSamsungIphone} euro goedkoper dan de Samsung.
            """)
    else:
        print(f""" 
            De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro
            De Iphone zit daar tussenin met: {iphonePrijs} Euro
            De Asus is het duurst, de telefoon kost: {asusPrijs} Euro

            Het advies is dus de Iphone te kopen. Deze is namelijk {verschilAsusIphone} euro goedkoper dan de Asus
            en {verschilSamsungIphone} euro goedkoper dan de Samsung.
            """)
else:
    if iphonePrijs > samsungPrijs:
        if samsungPrijs > asusPrijs:
            print(f""" 
            De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
            De Samsung zit daar tussenin met: {samsungPrijs}
            De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro
            """)

            if verschilIphoneSamsung <= 50:
                print(f'Het advies is dus de Iphone te kopen. Deze is namelijk maar {verschilIphoneSamsung} euro duurder dan de Samsung en {verschilIphoneAsus} duurder dan de Asus')
            else:
                print(f'Het advies is dus de Asus te kopen. Deze is namelijk {verschilIphoneAsus} euro goedkoper dan de iphone en {verschilSamsungAsus} euro goedkoper dan de Samsung')
    
        else:
             print(f""" 
            De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro
            De Asus zit daar tussenin met: {asusPrijs}
            De Iphone is het duurst, de telefoon kost: {iphonePrijs} Euro
            """)
             if verschilIphoneSamsung <= 50:
                print(f'Het advies is dus de Iphone te kopen. Deze is namelijk maar {verschilIphoneSamsung} euro duurder dan de Samsung en {verschilIphoneAsus} duurder dan de Asus')

             else:
                print(f'Het advies is dus de Samsung te kopen. Deze is namelijk {verschilSamsungIphone} euro goedkoper dan de iphone en {verschilAsusSamsung} euro goedkoper dan de Asus')

    else:
        if iphonePrijs > asusPrijs and verschilIphoneAsus <100:
            print(f""" 
            De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
            De Iphone zit daar tussenin met: {iphonePrijs}
            De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

            Het advies is de Asus te kopen. Deze is namelijk {verschilIphoneAsus} euro goedkoper dan de Iphone en {verschilSamsungAsus} goedkoper dan de Samsung.
            """)

        elif iphonePrijs > asusPrijs and verschilIphoneAsus > 100:
            print(f""" 
            De Asus is het goedkoopst, de telefoon kost: {asusPrijs} Euro
            De Iphone zit daar tussenin met: {iphonePrijs}
            De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

            Het advies is de Iphone te kopen. Deze is namelijk {verschilIphoneAsus} maar euro duurder dan de Asus en {verschilIphoneSamsung} goedkoper dan de Samsung.
            """)
        
        else:
            if asusPrijs < samsungPrijs:
                print(f""" 
                De Iphone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro
                De Asus zit daar tussenin met: {asusPrijs}
                De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro

                Het advies is de Iphone te kopen. Deze is namelijk {verschilAsusIphone} euro goedkoper dan de Asus en {verschilIphoneSamsung} goedkoper dan de Samsung.
                """)
            else:
                print(f""" 
                De Iphone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro
                De Samsung zit daar tussenin met: {samsungPrijs}
                De Asus is het duurst, de telefoon kost: {asusPrijs} Euro

                Het advies is de Iphone te kopen. Deze is namelijk {verschilAsusIphone} euro goedkoper dan de Asus en {verschilIphoneSamsung} goedkoper dan de Samsung.
                """)