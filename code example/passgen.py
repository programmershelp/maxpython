#!/usr/bin/python

import random
import string

def randomPassword(stringLength=16):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Random password is ", randomPassword() )
print ("Random password is ", randomPassword(14) )
print ("Random password is ", randomPassword(18) )