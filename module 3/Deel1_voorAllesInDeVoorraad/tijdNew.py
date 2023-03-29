ochtendtijd = 1
ochtendRange = range(1, 13)
middagtijd = 1
middagRange = range(1, 13)

for ochtendtijd in ochtendRange:
    print(ochtendtijd, 'AM')
    if ochtendtijd >= 12:
        for middagtijd in middagRange:
            print(middagtijd, 'PM')
