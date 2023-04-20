dagen = ('Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'zondag')

week = 'Dit zijn alle dagen van de week: '
for x in dagen:
    week += ' ' + x + ','
print(week)

werkdagen = 'Dit zijn alle werkdagen:'
for y in dagen[0:5]:
    werkdagen += ' ' + y + ','

print(werkdagen)

weekendDagen = 'Dit zijn alle dagen in het weekend: '
for z in dagen[5:8]:
    weekendDagen += ' ' + z + ','

print (weekendDagen)

omgekeerd = 'Dit zijn alle dagen in de week omgekeerd: '
for x in dagen[::-1]:
    omgekeerd += ' ' + x + ','

print (omgekeerd)

werkdagen_omgekeerd = 'Dit zijn alle werkdagen omgekeerd: '
for y in dagen[4::-1]:
    werkdagen_omgekeerd += ' ' + y + ','

print(werkdagen_omgekeerd)

weekendDagen_omgekeerd = 'Dit zijn alle weekend dagen omgekeerd: '
for z in dagen [7:4:-1]:
    weekendDagen_omgekeerd += ' ' + z + ','

print(weekendDagen_omgekeerd)