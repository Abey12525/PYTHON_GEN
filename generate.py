#!/usr/bin/env python

import random

MAXNO = 10 ** 7

n = random.randint(MAXNO/2, MAXNO)
print "Generating %d integers"%n
nos = range(1, n)
print "Shuffling"
random.shuffle(nos)
print "Writing to input.list"
with open("input.list","w") as f:
    for i in nos:
        f.write("%d\n"%i)

print "Done"
        
    
