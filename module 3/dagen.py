dagen = ("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag")

weekzin = "Alle dagen van de week zijn:"
for x in dagen:
    weekzin +=" " + x + ","

print(weekzin)
    

werkdagen = "Dit zijn alle werkdagen:"
for y in dagen[0:5]:
    werkdagen +=" " + y + ","

print (werkdagen)


weekenddagen = "Dit zijn alle weekend dagen:"
for z in dagen[5:8]:
    weekenddagen+=" " + z + ","

print(weekenddagen)

weekdagen_omgekeerd = "Dit zijn alle dagen van de week omgekeerd:"
for a in dagen[::-1]:
    weekdagen_omgekeerd+=" " + a + ","

print(weekdagen_omgekeerd)

werkdagen_omgekeerd = "Dit zijn alle werkdagen omgekeerd"
for b in dagen[4::-1]:
    werkdagen_omgekeerd+=" " + b + ","

print(werkdagen_omgekeerd)

weekenddagen_omgekeerd = "Dit zijn alle weekend dagen omgekeerd:"
for c in dagen[7:4:-1]:
    weekenddagen_omgekeerd +=" " + c + ","

print(weekenddagen_omgekeerd)
# print("Dit zijn alle werkdagen:")
# for y in (dagen[0:5]):
#     print(y)

# print("Dit zijn de Weekend dagen: ")
# for z in (dagen[5:8]):
#     print(z)

# print("Dit zijn alle dagen van de week omgekeerd: ")
# for x in (dagen[::-1]):
#     print(x)

# print("Dit zijn alle werkdagen omgekeerd: ")
# for y in (dagen[4::-1]):
#     print(y)

# print("Dit zijn alle weekend dagen omgekeerd: ")
# for z in (dagen[7:4:-1]):
#     print(z)
