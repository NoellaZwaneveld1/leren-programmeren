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




if __name__ == '__main__':
    pass