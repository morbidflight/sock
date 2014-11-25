############################################
# Fiddlesticks ult, a novel.
# Generated text based on the feeling of 
# playing fiddlesticks and ulting
# because crowstorm.
# by morbidflight for NaNoGenMo 2014
# https://github.com/dariusk/NaNoGenMo-2014
############################################ 

import random

# constants
word = "caw"
endpunc = [".", "!", "?", "..."]
midpunc = [" -", ",", ":", ";"]
allpunc = midpunc + endpunc
n = 100 # how many words do you want

# variables
sent = []
upper = True
x = 0

def addpunc(s):    # adds punctuation to the end of a word, maybe
    result = s
    if random.random() <= 0.1:
        result += random.choice(allpunc)
    result += " "
    return result

while True:    # creates the body of the novel
    # checks to see if it's > n iterations and end of a sentence
    if x > n and upper:
        break
    # checks whether the flag for capitalization is set, if it is, 
    # uses title case, if not, just appends with possible punctuation
    if upper:
        sent.append(addpunc(word).title())
    else:
        sent.append(addpunc(word))
    # checks the capitalization of the last word added, sets flag
    if sent[x][3] in endpunc:
        upper = True
        if random.random() <= 0.1:
            sent[x] += "\n" # occasionally throws in a paragraph break
    else:
        upper = False
    x += 1

print "".join(sent)
print "An enemy has been slain."
