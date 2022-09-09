a = input('Welk getal is a? ')
b = input('Welk getal is b? ')

if a > b:
    max = max(a)
    print(f'A is het grootste getal: {max}')

elif a < b:
    min = min(a)
    print(f'A is het kleinste getal: {min}')

else:
    print('A en b zijn even groot')