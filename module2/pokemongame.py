import time
import sys
import random 

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
""") #Vraagt welke starter je wilt

pokemonStarter = int(input())

starterMoltres = 'Moltres'
moltresType = 'Fire and flying'
moltresHeight = '2.0 M'
moltresWeight = '60.0 KG'

starterQuagsire = 'Quagsire'
quagsireType = 'Water and ground'
quagsireHeight = '1.4 M'
quagsireWeight = '75. 0 KG'

starterMeganium = 'Meganium'
meganiumType = 'Grass'
meganiumHeight = '1.8 M'
meganiumWeight = '100.5 KG'

if pokemonStarter == 1: #als je 1 heb gekozen laat hij zien dat je Moltres heb gekozen en laat hij alle stats van die pokemon zien
    pokemonStarter = 'Moltres'  #koppelt Moltres aan pokemon starter

    delay_printBio (f""" 
        You chose {starterMoltres}, the {moltresType} type pokemon!!
        
        PokeDex entry No. 146

        |Flame pokemon|
        Type   | {moltresType}
        Height | {moltresHeight}
        Weight | {moltresWeight}
        
        Ability: Flame body
                Contact with the pokemon may burn the attacker

        Base stats:
            HP         : 90
            Attack     : 100
            Defense    : 100
            SP.Attack  : 125
            SP.Defense : 85
            Speed      : 90
                Total: 580

        Move set:

        Ember (40 power, 100 accuracy)| FIRE:
            Deals damage and has a 10% chance of burning the target

        Air slash (75 power, 100 accuracy)| FLYING:
            Deals damage and has a 30% of causing the target to flinch

        Hurricane (110 power, 70 accuracy)| FLYING:
            Deals damage and has a 30% chance of confusing the target

        Endure (stat move)| NORMAL:
            Allows the user to survive all attacks during the turn with atleast 1 hp
    """) #zorgt dat de bio met delay getyped wordt, net zoals bij de oude pokemon games

elif pokemonStarter == 2:#als je 2 heb gekozen laat hij zien dat je Quagsire heb gekozen en laat hij alle stats van die pokemon zien
    pokemonStarter = 'Quagsire' #koppelt Quagsire aan pokemonStarter

    delay_printBio (f"""
    You chose {starterQuagsire}, the {quagsireType} type pokemon!!
    
    PokeDex entry No. 146

    |Flame pokemon|
    Type   | {quagsireType}
    Height | {quagsireHeight}
    Weight | {quagsireWeight}
    
    Ability: Water absorb
             A Pokémon with Water Absorb heals 1/4 of its maximum HP when hit by a Water-type attack.

    Base stats:
        HP         : 95
        Attack     : 85
        Defense    : 85
        SP.Attack  : 65
        SP.Defense : 65
        Speed      : 35 
            Total: 430

    Move set:

    Water gun(40 power, 100 accuracy)| WATER
	    Deals damage with no additional effect

    Slam(80 power, 75 accuracy)| NORMAL
	    Deals damage with no additional effect

    Earthquake(100 power, 100 accuracy)| GROUND
	    Deals damage, and will hit with double power if the opponent is underground due to dig

    Haze(stat move)| ICE
	    Resets all stat changes
    """)#zorgt dat de bio met delay getyped wordt, net zoals bij de oude pokemon games

elif pokemonStarter == 3:#als je 3 heb gekozen laat hij zien dat je Meganium heb gekozen en laat hij alle stats van die pokemon zien
    pokemonStarter = 'Meganium'#koppelt Meganium aan pokemonStarter

    delay_printBio(f"""
    You chose {starterMeganium}, the {meganiumType} type pokemon!!
    
    PokeDex entry No. 146

    |Flame pokemon|
    Type   | {meganiumType}
    Height | {meganiumHeight}
    Weight | {meganiumWeight}
    
    Ability: Water absorb
             A Pokémon with Water Absorb heals 1/4 of its maximum HP when hit by a Water-type attack.

    Base stats:
        HP         : 95
        Attack     : 85
        Defense    : 85
        SP.Attack  : 65
        SP.Defense : 65
        Speed      : 35
            Total: 525

    Move set:

    Magical leaf (60 power, 100 accuracy) | Grass
        Deals damage and ignores changes to the Accuracy and Evasion stats. 
        However, it will not hit pokemon during the invulnerable stage of Bounce, Dig, Dive, Fly,
        Shadow Force, or sky drop

    Body Slam (80 power, 75 accuracy) | NORMAL
        Deals damage and has a 30%  chance of paralyzing the target.
        Electric type pokemon, those with the ability Limber or those behind a substitute cannot
        be paralyzed. 
        If the target has used Minimize, Body slam ignores accuracy and deals double damage 

    Solar beam (120 power, 100 accuracy )| GRASS
        he user of Solar Beam will absorb light on the first turn. On the second turn, Solar Beam deals damage.
        During intense sunlight or when holding a Power Herb, Solar Beam executes in one turn. During rain, hail or a sandstorm its power decreases by 50%.

    Poison powder (stat move) | POISON
        Causes the target to become poisoned.
        Poisoned pokemon lose 1/8 of their maximum HP each turn. 
        Poison or steel type pokemon, those with the ability immunity or those behind a substitute cannot be poisoned
    """)#zorgt dat de bio met delay getyped wordt, net zoals bij de oude pokemon games

print(pokemonStarter)