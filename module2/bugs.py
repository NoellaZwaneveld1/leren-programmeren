leeftijd = input("Hoe oud ben je?") #vraagt om de leeftijd, maar omdat het een string is geeft hij een error

if leeftijd < 18 or leeftijd = 18: #wilt weten of de persoon achtien of jonger is, maar omdat er maar 1 = staat werkt het niet
    print"Je bent te jong" # () vergeten

else:
print("je bent welkom")#geen indentation

elif leeftijd < 10: # de elif komt na de else dus werkt het niet
    print()