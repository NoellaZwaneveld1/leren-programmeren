a = input('Welk getal is a? ')
b = input('Welk getal is b? ')

if a > b:
    min = min(b)
    max = max(a)
    print(f'A is het grootste getal: {max}')
    
    print(f"""
    Het minimum is:  {min}
    Het maximum is:  {max}    
    """)

elif a < b:
    min = min(a)
    max = max(b)
    print(f'A is het kleinste getal: {min}')

    print(f"""
    Het minimum is:  {min}
    Het maximum is:  {max}    
    """)

else:
    print('A en b zijn even groot')

   