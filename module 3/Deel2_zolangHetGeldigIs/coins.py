# name of student:  Noëlla
# number of student: 99038192
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #hier voer je in hoeveel je moet betalen in euro's, het programma maakt er centen van (*100)
paid = int(float(input('Paid amount: ')) * 100) #hier voor je in hoeveel je al heb betaald in euro's, ook hier maakt het programma centen van
change = paid - toPay #change is paid min topay

if change > 0: #als change groter is dan 0
  coinValue = 500 #coinvalue is gelijk aan 50
  
  while change > 0 and coinValue > 0: #zolang change en coinvalue groter zijn dan 0
    nrCoins = change // coinValue # floor devision, rond het getal op naar een heel getal

    if nrCoins > 0: #als nrcoins groter zijn dan 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #print de hoeveelheid coins van de volgende coinvalue
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #vraagt hoeveel coins van de coin value je teruggeef 
      change -= nrCoinsReturned * coinValue #het programma rekent eerst uit wat nrcoinsreturned keer coinvalue is, daarna haalt hij dat van change af

# comment on code below: 
# het begint met de coinvalue is 50, hij vraagt hoeveel munten van 50 je teruggeef. daarna maakt hij van de value 20.
#dan gaat hij vragen hoeveel coins van 20 je teruggeeft. daarna wordt de value verandert naar 10
# hoeveel munten van 10 geef je terug. daarna wordt de value omgezet naar 5, daarna zijn de 2 en 1 centen aan de beurt. als dat allemaal is gedaan is de coin value 0
    
    if coinValue == 500:
      coinValue5Euro = 500
      euro5Returned = nrCoinsReturned
      coinValue = 300
    elif coinValue == 300:
      coinValue3Euro = 300
      euro3Returned = nrCoinsReturned
      coinValue = 200
    elif coinValue == 200:
      coinValue2Euro = 200
      euro2Returned = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
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
3 Euro:                   X{euro3Returned}
2 Euro:                   X{euro2Returned}
50 Cent:                  X{cent50Returned}
20 Cent:                  X{cent20Returned}
10 Cent:                  X{cent10Returned}
5 Cent:                   X{cent5Returned}
2 Cent:                   X{cent2Returned}
1 Cent:                   X{cent1Returned}
""")
if change > 0: #als de change groter is dan 0 laat hij zien hoeveel centen er niet zijn teruggegeven.
  print('Change not returned: ', str(change) + ' cents')
else:
  print('All change has been returned')