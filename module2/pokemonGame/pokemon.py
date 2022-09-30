import time #zorgt dat je met tijd kan werken
import sys #bevat alle systeem gerelateerde functies
import random #zorgt dat je random getallen kan opvragen
import numpy as py

def delay_print(s):
    #print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)

delay_print ('WHat is your name? ')

trainerName = input()

delay_print(f"""
Welcome trainer {trainerName}, are you ready to start your Pokémon adventure?
1] Yes
2] No
""")

start = int(input())

if start == 2:
    exit()

grassPokémon1 = 'Gossifleur'
grassPokémon2 = 'Eldegoss'

delay_print(f"""
Your adventure starts at the first gym, the grass gym.
The gym leaders first Pokémon is {grassPokémon1}, the grass type. 
Your team consists of:
1] Mankey, Fighting type
2] Rookidee, Flying type
3] Geodude, Rock and Ground type
4] Growlithe, Fire type
5] Sandshrew, Ground type
6] Rattata, Normal type
Which Pokémon will you choose to defeat {grassPokémon1}?
""")

gym1_battle1 = int(input())
gymBadges = 0

if gym1_battle1 == 1:
    currentPokemon = 'Mankey'
    print(f"Your {currentPokemon}'s attacks are neutral against {grassPokémon1}. This is going to be a tough battle.")
    time.sleep (0.5)
    battle1Decision = random.randint(0,100)
    
    if battle1Decision <= 80:
        print(f'You have defeated the {grassPokémon1}') # f = format
    
    else:
        print(f"""
        Unfortunately your {currentPokemon} wasn't strong enough to defeat the {grassPokémon1}.
        You have {gymBadges} gym badges
        """)
        exit()
      
elif gym1_battle1 == 2:
    currentPokemon = 'Rookidee'
    print(f"Your {currentPokemon}'s attacks are very effective against {grassPokémon1}. ")
    time.sleep (0.5)
    print(f'You have defeated the {grassPokémon1}')

elif gym1_battle1 == 3:
    currentPokemon = 'Geodude'
    print(f"Your {currentPokemon}'s attacks are very weak against {grassPokémon1}. ")
    time.sleep (0.5)

    print(f"""
    Unfortunately your {currentPokemon} wasn't strong enough to defeat the {grassPokémon1}.
    You have {gymBadges} gym badges
    """)
    exit()
    
elif gym1_battle1 == 4:
    currentPokemon = 'Growlithe'
    print(f"Your {currentPokemon}'s attacks are very effective against {grassPokémon1}.")
    time.sleep(0.5)
    print(f'You have defeated the {grassPokémon1}')

elif gym1_battle1 == 5:
    currentPokemon = 'Sandshrew'
    print(f"Your {currentPokemon}'s attacks are very weak against {grassPokémon1}. ")
    time.sleep (0.5)

    print(f"""
    Unfortunately your {currentPokemon} wasn't strong enough to defeat the {grassPokémon1}.
    You have {gymBadges} gym badges
    """)
    exit()

  

elif gym1_battle1 == 6:
    currentPokemon = 'Rattata'
    print(f"Your {currentPokemon}'s attacks are neutral against {grassPokémon1}. This is going to be a tough battle.")
    time.sleep (0.5)
    battle1Decision = random.randint(0,100)
    
    if battle1Decision <= 80:
        print(f'You have defeated the {grassPokémon1}')
    
    else:
        print(f"""
        Unfortunately your {currentPokemon} wasn't strong enough to defeat the {grassPokémon1}.
        You have {gymBadges} gym badges
        """)
        exit()

delay_print(f"""
Well done, you have defeated the gym leaders first Pokémon! The gym leader has only one Pokémon left.
What will you do?
1] Heal your Pokémon 
2] Continue like this
""")

gym1_battle2 = int(input())

if (gym1_battle2 == 1 and currentPokemon == 'Mankey'):
    print("You healed your Pokémon...")
    time.sleep(0.1)
    print(f"Your {currentPokemon}'s attacks are neutral against {grassPokémon2}. This is going to be a tough battle.")
    time.sleep (0.5)
    battle1Decision = random.randint(0,100)
    
    if battle1Decision <= 80:
        print(f'You have defeated the {grassPokémon2}')
        gymBadges = 1
        time.sleep(0.1)
        print(f'Congratulations! You now have {gymBadges} Gym badge!')
    
    else:
        print(f"""
        Unfortunately your {currentPokemon} wasn't strong enough to defeat the {grassPokémon2}
        """)
        exit()

elif (gym1_battle2 == 2 and currentPokemon == 'Mankey'):
    print("You didn't heal your Pokémon...")
    time.sleep(0.1)
    print(f"Your {currentPokemon}'s attacks are neutral against {grassPokémon2}. This is going to be a tough battle.")
    time.sleep (0.5)
    battle1Decision = random.randint(0,100)
    
    if battle1Decision <= 60:
        print(f'You have defeated the {grassPokémon2}')
        gymBadges = 1
        time.sleep(0.1)
        print(f'Congratulations! You now have {gymBadges} Gym badge!')
    
    else:
        print(f"""
        Unfortunately your {currentPokemon} wasn't strong enough to defeat the {grassPokémon2}.
        You have {gymBadges} gym badges
        """)
        exit()

if (gym1_battle2 == 1 and currentPokemon == 'Rookidee'):
    print("You healed your Pokémon...")
    time.sleep(0.1)
    print(f"Your {currentPokemon}'s attacks are very effective against {grassPokémon1}. ")
    time.sleep (0.5)
    print(f'You have defeated the {grassPokémon1}')

    gymBadges = 1
    time.sleep(0.1)
    print(f'Congratulations! You now have {gymBadges} Gym badge!')

elif (gym1_battle2 == 2 and currentPokemon == 'Rookidee'):
     print("You didn't heal your Pokémon...")
     time.sleep(0.1)
     print(f"Your {currentPokemon}'s attacks are very effective against {grassPokémon1}. ")
     time.sleep (0.5)
     battle1Decision = random.randint(0,100)

     if battle1Decision <= 80:
        print(f'You have defeated the {grassPokémon2}')
        gymBadges = 1

        time.sleep(0.1)
        print(f'Congratulations! You now have {gymBadges} Gym badge!')

     else:
        print(f"""
        Unfortunately your {currentPokemon} wasn't strong enough to defeat the {grassPokémon2}.
        You have {gymBadges} gym badges
        """)
        exit()

if (gym1_battle2 == 1 and currentPokemon == 'Growlithe'):
    print("You healed your Pokémon...")
    time.sleep(0.1)
    print(f"Your {currentPokemon}'s attacks are very effective against {grassPokémon2}.")
    time.sleep(0.5)
    print(f'You have defeated the {grassPokémon2}')
    gymBadges = 1

    time.sleep(0.1)
    print(f'Congratulations! You now have {gymBadges} Gym badge!')

elif (gym1_battle2 == 2 and currentPokemon == 'Growlithe'):
    print("You didn't heal your Pokémon...")
    time.sleep(0.1)
    print(f"Your {currentPokemon}'s attacks are very effective against {grassPokémon2}.")
    time.sleep(0.5)
    battle1Decision = random.randint(0,100)


    if battle1Decision <= 80:
        print(f'You have defeated the {grassPokémon2}')
        gymBadges = 1

        time.sleep(0.1)
        print(f'Congratulations! You now have {gymBadges} Gym badge!')

    else:
        print(f"""
        Unfortunately your {currentPokemon} wasn't strong enough to defeat the {grassPokémon2}.
        You have {gymBadges} gym badges
        """)
        exit()

if (gym1_battle2 == 1 and currentPokemon =='Rattata'):
    print("You healed your Pokémon...")
    time.sleep(0.1)
    print(f"Your {currentPokemon}'s attacks are neutral against {grassPokémon2}. This is going to be a tough battle.")
    time.sleep (0.5)
    battle1Decision = random.randint(0,100)
    
    if battle1Decision <= 80:
        print('You have defeated the Gossifleur')
        gymBadges = 1

        time.sleep(0.1)
        print(f'Congratulations! You now have {gymBadges} Gym badge!')
    
    else:
        print(f"""
        Unfortunately your {currentPokemon} wasn't strong enough to defeat the {grassPokémon1}.
        You have {gymBadges} gym badges
        """)
        exit()

elif (gym1_battle2 == 2 and currentPokemon == 'Rattata'):
     print("You didn't heal your Pokémon...")
     time.sleep(0.1)
     print(f"Your {currentPokemon}'s attacks are neutral against {grassPokémon2}. This is going to be a tough battle.")
     time.sleep (0.5)
     battle1Decision = random.randint(0,100)

     if battle1Decision <= 60:
        print(f'You have defeated the {grassPokémon2}')
        gymBadges = 1

        time.sleep(0.1)
        print(f'Congratulations! You now have {gymBadges} Gym badge!')
    
     else:
        print(f"""
        Unfortunately your {currentPokemon} wasn't strong enough to defeat {grassPokémon2}.
        You have {gymBadges} gym badges
        """)
        exit()