import pronouncing
import random

text = 'this is the sample text to replace certain words in'
out = list()

for word in text.split():
    rhymes = pronouncing.rhymes(word)
    if len(rhymes) > 0:
        out.append(random.choice(rhymes))
    else:
        out.append(word)

print (' '.join(out))