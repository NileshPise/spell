#!/usr/bin/env python
# coding: utf-8

# In[28]:



# Importing Required Libraries
import enchant
import jamspell
import numpy as np
from textblob import TextBlob
from spellchecker import SpellChecker

class AutoSpellChecker(object):
    
    def __init__(self):
        # create dictionary for the language
        # in use(en_US here)
        self.dict = enchant.Dict("en_US")
        self.spell = SpellChecker()
        self.corrector = jamspell.TSpellCorrector()
        self.corrector.LoadLangModel('en.bin')


    def spell_check_for_word(self, word):
        # if return false it means that word spelling is correct and if return true then spelling is incorrect
        if self.enchant_spell_check(word= word) == False or self.spellchecker_spell_check(word= word) is not None:
            return True
        else:
            return False
        
    def enchant_spell_check(self, word):
        # find those words that may be misspelled 
        # if word is correct then return true
        return self.dict.check(word)
    
    def spellchecker_spell_check(self, word):
        # if word is wrong then it will return word
        return self.spell.unknown([word])
            
        
    def enchant_responce(self, word):
        words_list = self.dict.suggest('conty')
        return words_list
    
    def spellchecker_responce(self, word):
        word_list1 = self.spell.candidates(word)
        return word_list1

    def jamspell_responce(self, word):
        list1 = [word]
        word_list2 = corrector.GetCandidates(list1, 0)
        return word_list2
    
    def textblob_responce(self, word):
        words_list3 = TextBlob(word)
        words = words_list3.correct()
        return words.words
    
    
    def correct_spell_suggestion(self, word):
        word_correct_suggestion_list = [item for item in self.textblob_responce(word= word)]
        word_correct_suggestion_list1 = self.enchant_responce(word= word)
        word_correct_suggestion_list2 = [item for item in self.spellchecker_responce(word= word)]
        word_correct_suggestion_list.extend(word_correct_suggestion_list2)
        word_correct_suggestion_list.extend(word_correct_suggestion_list1)
        word_correct_suggestion_list.extend(self.jamspell_responce(word= word))
        return word_correct_suggestion_list

