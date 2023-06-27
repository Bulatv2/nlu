# nlu

ner (ru)

from nlp.words import Words
from ner import Ner
import corpus
with open("data.txt", "r") as file:
    text = file.read()
nr = corpus.ner()
"""tokenize string to words"""
tokword = Words(text)
tokwordload = tokword.load()
"""ner classification"""
instn = Ner(*nr)
n = instn.load(tokwordload)
print("\nner classification:\n", n)

requirements: nlp from my repository
