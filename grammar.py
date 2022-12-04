#!/usr/bin/env python3

import nltk
from nltk.corpus import wordnet as wn

nouns = []
verbs = []
adjective = []
adverbs = []
sat_adjectives = []

for synset in list(wn.all_synsets()):
	lemma = synset.lemmas()[0]
	word = lemma.name()
	if len(word) < 3 or len(word) > 8:
		continue
	if synset.pos() == 'n':
		nouns.append(word)

print(len(nouns))
