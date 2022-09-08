small = int(input('Hoeveel small pizzas wilt u?' ))
totaalSmall = small * 9.94

medium = int(input('Hoeveel medium pizzas wilt u? '))
totaalMedium = medium * 10.99

large = int(input('Hoeveel large pizzas wilt u?'))
totaalLarge = large * 14.49

print('Dit is uw bestelling!')
print('U heeft ', small, 'small pizzas, dit kost', totaalSmall, 'euros')
print('U heeft ', medium, 'medium pizzas, dit kost', totaalMedium, 'euros')
print('U heeft ', large, 'large pizzas, dit kost', totaalLarge, 'euros')

print('De totaal prijs is: ', totaalSmall + totaalMedium + totaalLarge, 'euros')

