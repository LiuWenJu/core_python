#coding=utf-8

import re, collections

def words(text):
    return re.findall('[a-z]+',text.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS=train(words(file('big.txt').read()))

alphabet = "abcdefghjklmnopqrstuvwxyz"

def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word)+1)]

