import time
import sys

#delay printing

def delay_print(s):
    #print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush
        time.sleep(0.10)

delay_print('Pokemon game!!!')
