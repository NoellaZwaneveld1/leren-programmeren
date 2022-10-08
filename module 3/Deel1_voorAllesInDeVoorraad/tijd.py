#opdracht 1 
# ochtendtijd = 1
# ochtendRange = range(1, 13)
# middagtijd = 1
# middagRange = range(1, 13)

# for ochtendtijd in ochtendRange:
#     print(ochtendtijd, 'AM')

# for middagtijd in middagRange:
#     print(middagtijd, 'PM')

#opdracht 2
ochtendtijd = 1
avondtijd = 1

while ochtendtijd <= 12:
    print(f'{ochtendtijd} AM')
    ochtendtijd = ochtendtijd + 1
    while ochtendtijd > 12:
        while avondtijd <= 12:
            print(f'{avondtijd} PM')
            avondtijd = avondtijd + 1