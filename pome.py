import random
from datetime import datetime

def makeline(words):
    line = ' '.join(words)
    line = line[0].upper() + line[1:] + '.'
    return line

def pome(phrase):
    words = phrase.split()
    while words:
    	for _ in range(3):
            print makeline(words)
            random.shuffle(words)
        print
        words.pop(random.randrange(len(words)))

random.seed(datetime.now().microsecond)
phrase = 'now is the time'
pome(phrase)
