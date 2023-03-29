ochtendtijd = 1
avondtijd = 1

while ochtendtijd <= 12:
    print(f"{ochtendtijd} AM")
    ochtendtijd +=1
    if ochtendtijd > 12:
        while avondtijd <=12:
            print(f"{avondtijd} PM")
            avondtijd +=1