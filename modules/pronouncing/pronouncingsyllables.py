import pronouncing
text = "this is the sample text to check"
phones = [pronouncing.phones_for_word(p)[0] for p in text.split()]
print (sum([pronouncing.syllable_count(p) for p in phones]))