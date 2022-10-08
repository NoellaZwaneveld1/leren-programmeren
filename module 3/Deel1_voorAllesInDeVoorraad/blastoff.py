# startLancering = 30
# lancering = range(30, -1, -1) #telt terug vanaf 30 met een stap van 1

# for startLancering in lancering:
#     print (startLancering)
#     if startLancering <= 0:
#         print ('De raket is gelanceerd')

startLancering = 30

while startLancering > 0:
    print(startLancering)
    startLancering = startLancering - 1

if startLancering == 0:
    print('De raket is gelanceerd')