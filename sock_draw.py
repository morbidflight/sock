import random
import sys

k = 'O'
p = '-'
last = 'k'

while (1):
    if last == k:
        last = p
    elif last == p:
        last = k
    else:
        last = random.choice([k, p])
    sys.stdout.write(last)
