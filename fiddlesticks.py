import random

word = "caw"
endpunc = [".", "!", "?", "..."]
midpunc = ["...", "-", ",", ":", ";"]

nov = random.randint(1, 100)

for x in range (0, nov):
    temp = random.randint(1, 10)
#    rtemp = random.randint(1, temp)
    sent = [word.title()]
    for y in range (0, temp):
        sent.append(word)
    print " ".join(sent),
    print random.choice(endpunc),

print "An enemy has been slain."
