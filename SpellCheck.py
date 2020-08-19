'''
Created by Vedant Christian
Created on 19 / 08 / 2020
'''
from spellchecker import *
from autocorrect import Speller

check = Speller(lang="en")
spell = SpellChecker()

mispelled = ("I am goof, waht abot yu").split()


for word in mispelled:
    print(spell.correction(word), end = " ")

print(check(str(mispelled)))