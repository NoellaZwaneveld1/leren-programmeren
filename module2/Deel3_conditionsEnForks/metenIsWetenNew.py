a = int(input("Vul een getal in: "))
b = int(input("Vul een getal in: "))

if a > b:
    max = a
    min = b
    print(f"A is het grootste getal {max}")

elif a < b:
    max = b 
    min = a
    print(f"A is het kleinste getal: {min}")

else:
    print("A en b zijn even groot")
    exit()

print(f"""
    Het minimum is: {min}
    Het maximum is: {max}
    """)
