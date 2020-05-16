#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for i in range(passLen):
        password+=characters[random.randint(0, len(characters))]
    
    return password