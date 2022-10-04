import time #returns number of seconds passed since epoch
import numpy as np
import sys #contains all system- related functions

#delay printing

def delay_print(s):
    #Print 1 letter tegelijk
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


#create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, hp='====================='): #built in function name for classes. Initialization for attributes 
    #save variables as attributes
     self.name = name
     self.types = types
     self.moves = moves
     self.attack = EVs ['ATTACK']
     self.defense = EVs ['DEFENSE']
     self.bars = 20 #health bars left for each pokemon


def fight(self, Pokemon2):
    #allow two pokemon to fight eachother

    #print fight information
    print('------POKEMON BATTLE------')
    print(f'\n{self.name}') #print de naam van de pokemon
    print('TYPE/', self.type) #print de type van de pokemon
    print('ATTACK/', self.attack) #print de attack EV van de pokemon
    print('DEFENSE/', self.defense) #print de defense EV van de pokemon
    print('LVL/', 3 *(1 + np.mean([self.attack, self.defense]))) #calculeert de level van de pokemon.het gemiddelde van de attack en defense + 1 * 3 
    print('\nVS')
    print(f'\n{Pokemon2.name}') #print de naam van de pokemon
    print('TYPE/', Pokemon2.type) #print de type van de pokemon
    print('ATTACK/', Pokemon2.attack) #print de attack EV van de pokemon
    print('DEFENSE/', Pokemon2.defense) #print de defense EV van de pokemon
    print('LVL/', 3 *(1 + np.mean([Pokemon2.attack, Pokemon2.defense]))) #calculeert de level van de pokemon.het gemiddelde van de attack en defense + 1 * 3 

    time.sleep(2) #wacht 2 seconden voordat de volgende text verschijnt

    #consider type advantages
    version = ['Fire', 'Water', 'Grass']
    for i,k in enumerate(version):
        if self.types == k:
            #both are the same type
            if Pokemon2.types == k:
               string_1_attack = 'Its not very effective...' 
               string_2_attack = 'Its not very effective...' 
            
            #pokemon2 is STRONG against pokemon1
            if Pokemon2.types == version[(i+1)%3]:
                Pokemon2.attack *=2
                Pokemon2.defense *=2
                self.attack /=2
                self.defense /=2
                string_1_attack = 'Its not very effective...' 
                string_2_attack = 'Its super effective!'

            #pokemon2 is weak
            if Pokemon2.types == version[(i+2)%3]:
                self.attack *=2
                self.defense *=2
                Pokemon2.attack /=2
                Pokemon2.defense /=2
                string_1_attack = 'Its super effective!'
                string_2_attack = 'Its not very effective...' 

    #now the actual battle
    #continue while the pokemon still have health
    while (self.bars > 0) and (Pokemon2.bars > 0):
        #print the health of each pokemon
        print(f'{self.name}\t\tHP\t{self.health}')
        print(f'{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n')

        print(f'Go {self.name}!')
        for i, x in enumerate(self.moves):
            print(f'{i+1}.', x)
        index = int(input('Pick a move:  '))
        delay_print(f'{self.name} used {self.moves[index-1]}')
        time.sleep1
        delay_print(string_1_attack)

        #determine damage
        Pokemon2.bars -= self.attack
        Pokemon2.health = ''

        #add back bars plus defensive boost
        for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
            Pokemon2.health += "="

        time.sleep(1)
        print(f'{self.name}\t\tHP\t{self.health}')
        print(f'{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n')
        time.sleep(.5)

        #Check to see if pokemon fainted

        if Pokemon2.bars <= 0:
            print(f'\n... {Pokemon2.name} fainted')
            break


            



if __name__ == '__main__':
    pass