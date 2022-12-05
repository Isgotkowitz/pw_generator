#!/usr/bin/env python3

import nltk
from nltk.corpus import wordnet as wn
from noSim import noSimiListFn
from textdistance import damerau_levenshtein as dl
import json
import os

nouns = {}
verbs = {}
adjectives = {}
adverbs = {}

n_count = 0
v_count = 0
a_count = 0
r_count = 0

for synset in list(wn.all_synsets()):
    lemma = synset.lemmas()[0]
    word = lemma.name()
    if len(word) < 3 or len(word) > 8:
        continue
    pos = synset.pos()
    if pos == 'n':
        nouns[n_count] = word
        n_count += 1
    elif pos == 'v':
        verbs[v_count] = word
        v_count += 1
    elif pos == 'a' or pos == 's':
        adjectives[a_count] = word
        a_count += 1
    elif pos == 'r':
        adverbs[r_count] = word
        r_count += 1

try:
    os.mkdir("jsons")
except FileExistsError as e:
    pass
except OSError as e:
    print(e)
    os.exit()

with open("jsons/nouns.json", "w") as noun_file:
    json.dump(nouns, noun_file)

with open("jsons/adjectives.json", "w") as adjective_file:
    json.dump(adjectives, adjective_file)

with open("jsons/verbs.json", "w") as verb_file:
    json.dump(verbs, verb_file)

with open("jsons/adverbs.json", "w") as adverb_file:
    json.dump(adverbs, adverb_file)


print("# maybe similar nouns: {}".format(len(nouns)))
print("# maybe similar verbs: {}".format(len(verbs)))
print("# maybe similar adjectives: {}".format(len(adjectives)))
print("# maybe similar adverbs: {}".format(len(adverbs)))

'''
nouns = noSimiListFn(dl, nouns)
verbs = noSimiListFn(dl, verbs)
adjectives = noSimiListFn(dl, adjectives)
adverbs = noSimiListFn(dl, adverbs)

print("# nouns: {}".format(len(nouns)))
print("# verbs: {}".format(len(verbs)))
print("# adjectives: {}".format(len(adjectives)))
print("# adverbs: {}".format(len(adverbs)))
'''
