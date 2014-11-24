############################################
# Fiddlesticks ult, a novel.
# Generated text based on the feeling of 
# playing fiddlesticks and ulting
# because crowstorm.
# by morbidflight for NaNoGenMo 2014
# https://github.com/dariusk/NaNoGenMo-2014
############################################ 

import random

word = "caw"
endpunc = [".", "!", "?", "..."]
midpunc = ["...", "-", ",", ":", ";"]

allpunc = endpunc + midpunc

sent = []

upper = True

def addpunc(s):    # adds punctuation to the end of a word, maybe
    result = s
    if random.random() <= 0.1:
        result += random.choice(allpunc)
    result += " "
    return result


for x in range (0, 100):    # adds the capitalized form based on punc
    if upper:
        sent.append(addpunc(word).title())
    else:
        sent.append(addpunc(word))
    if sent[x][3] in endpunc:
        upper = True
    else:
        upper = False

print "".join(sent),
print "An enemy has been slain."
