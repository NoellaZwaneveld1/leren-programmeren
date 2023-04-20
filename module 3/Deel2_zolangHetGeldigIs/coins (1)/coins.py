# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #het aantal euro dat je moet betalen, wordt omgerekend naar cent
paid = int(float(input('Paid amount: ')) * 100) #het aantal euro dat je heb betaalt, wordt omgerekend naar cent
change =  paid - toPay #wisselgeld = wat je heb betaalt - wat je nog moet betalen

if change > 0: #als het wisselgeld meer is dan 0 
  coinValue = 500 #coinvalue = 50 cent
  
  while change > 0 and coinValue > 0: #wanneer change meer dan 0 is en coinvalue ook meer dan 0 is
    nrCoins = change // coinValue # floor devision, rond het getal op naar een heel getal

    if nrCoins > 0: #als nrcoins meer is dan 0 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #print hoeveel munten er maximaal van die coinvalue gegeven kan worden
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #vraagt hoeveel munten je geeft
      change -= nrCoinsReturned * coinValue #change = hoeveel munten je geeft * de value van de munten

# comment on code below: nadat de 50 munten zijn gedaan gaat het programma door todat het uiteindelijk bij 0 uitkomt
    if coinValue == 500:
      coinValue5Euro = 500
      euro5Returned = nrCoinsReturned
      coinValue = 200 
    elif coinValue == 200:
      coinValue2Euro = 200
      euro2Returned = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      coinValue1Euro = 100
      euro1Returned = nrCoinsReturned
      coinValue = 50
    if coinValue == 50:
      coinValue50Cent = 50
      cent50Returned = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      coinValue20Cent = 20
      cent20Returned = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      coinValue10Cent = 10
      cent10Returned = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      coinValue5Cent = 5
      cent5Returned = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      coinValue2Cent = 2
      cent2Returned = nrCoinsReturned
      coinValue = 1
      coinValue1Cent = 1
    else:
      cent1Returned = nrCoinsReturned
      coinValue = 0


print(f""" Amount of change returned:
5 Euro:                   X{euro5Returned} 
2 Euro:                   X{euro2Returned}
2 Euro:                   X{euro2Returned}
50 Cent:                  X{cent50Returned}
20 Cent:                  X{cent20Returned}
10 Cent:                  X{cent10Returned}
5 Cent:                   X{cent5Returned}
2 Cent:                   X{cent2Returned}
1 Cent:                   X{cent1Returned}
""")
if change > 0: #als change meer dan 0 is
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')