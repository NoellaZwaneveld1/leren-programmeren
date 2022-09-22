import time
import sys
import random
import pokemonBios
from urllib import robotparser 

#delay printing

def delay_print(s):
    #print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)

def delay_printBio(s):
    #print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

delay_print ('What is your name? ')

trainerName = input() #slaat je naam op in trainerName

delay_print (f"""
Welkom pokemon trainer {trainerName}! choose your starter!
1] Moltres, fire and flying type
2] Quagsire, Water and ground type 
3] Meganium, grass type
Pick carefully! This is the Pokemon you will stick with for the rest of your journey!
""") #Vraagt welke starter je wilt

pokemonStarter = int(input())

moltresBio = pokemonBios.moltresBio
quagsireBio = pokemonBios.quagsireBio
meganiumBio = pokemonBios.meganiumBio

if pokemonStarter == 1: #als je 1 heb gekozen laat hij zien dat je Moltres heb gekozen en laat hij alle stats van die pokemon zien
    pokemonStarter = 'Moltres'  #koppelt Moltres aan pokemon starter
    delay_printBio (moltresBio) #zorgt dat de bio met delay getyped wordt, net zoals bij de oude pokemon games

elif pokemonStarter == 2:#als je 2 heb gekozen laat hij zien dat je Quagsire heb gekozen en laat hij alle stats van die pokemon zien
    pokemonStarter = 'Quagsire' #koppelt Quagsire aan pokemonStarter
    delay_printBio (quagsireBio)#zorgt dat de bio met delay getyped wordt, net zoals bij de oude pokemon games

elif pokemonStarter == 3:#als je 3 heb gekozen laat hij zien dat je Meganium heb gekozen en laat hij alle stats van die pokemon zien
    pokemonStarter = 'Meganium'#koppelt Meganium aan pokemonStarter
    delay_printBio(meganiumBio)#zorgt dat de bio met delay getyped wordt, net zoals bij de oude pokemon games

delay_print(f"""Your pokemon adventure will start now! You leave your hometown Postwick and make your way to the first Gym, the grass Gym,
with your trusted starter {pokemonStarter}. 

You reach route 1, what will you do?
1] Run through the grass until you encounter a new pokémon to add to your team
2] Try to avoid the grass as much as possible, i don't need a second pokemon in my team yet!
""")

route1_choice = input()

skwovet = ("""
PokeDex entry No. 819

     |Cheeky Pokémon|
     Type   | Normal
     Height | 0.3 M
     Weight | 2.5 KG

Ability: Gluttony
                 A Pokémon with Gluttony will use a pinch berry when its HP drops to 50%,
                 rather than the usual 25%.

         Base stats:
             HP         : 70
             Attack     : 55
             Defense    : 55
             SP.Attack  : 35
             SP.Defense : 35
             Speed      : 25
                 Total: 275
""")

rookidee = ("""
PokeDex entry No. 821

     |Tiny Bird Pokémon|
     Type   | Flying
     Height | 0.2 M
     Weight | 1.8 KG

Ability: Unnerve
                 Makes the foe nervous and unable to eat Berries.

         Base stats:
             HP         : 38
             Attack     : 47
             Defense    : 35
             SP.Attack  : 33
             SP.Defense : 35
             Speed      : 57
                 Total: 245
""")
wooloo = ("""
PokeDex entry No. 831

     |Sheep Pokémon|
     Type   | Normal
     Height | 0.6 M
     Weight | 6.0 KG

Ability: Run away
                 Run Away allows the bearer to flee a battle with a wild Pokémon without fail,
                 even if the opposing Pokémon has used a move like Mean Look or Bind, 
                 or has an ability such as Arena Trap.

         Base stats:
             HP         : 42
             Attack     : 40
             Defense    : 55
             SP.Attack  : 40
             SP.Defense : 45
             Speed      : 48
                 Total: 270
""")

if route1_choice == 1:
    grassEncounter_route1 = ['Skwovet', 'Rookidee', 'Wooloo', 'Nickit']
    route1_pokémon = random.choice(grassEncounter_route1)
    print(f"""
    You have encountered a wild {route1_pokémon}! What will you do?
    1] Catch it!
    2] Run away
    """)
    grassEncounter_choice = input()

    if grassEncounter_choice == 1:
        print(f'You have caught {route1_pokémon}')
    
        if route1_pokémon == 'Skwovet':
            print(skwovet)

        elif route1_pokémon == 'Rookidee':
            print(rookidee)
        
        elif route1_pokémon == 'Wooloo':
            print(wooloo)

    else:
        print(f"""
        You ran away from the wild {route1_pokémon} and left route 1 without
        adding a new pokemon to your team!
        """)

elif route1_choice ==2:
    shadowEncounter_route1 = ['Blipbug', 'Caterpie', 'Grubbin', 'Hoothoot'] 