"""
Use 80/20 rule to hack language learning 
(Check TikTok faves)
Learn 20% of words that are used 80% of the time

- most common irregular and regular verbs (50 each)
- pronouns
- swear words
- present, past, future tenses (all - simple)
- 100 most common words (girl, table, live etc...)
- 20 most common expressions (omg etc...)
- prepositions & connectors
- question words (where etc..)
"""

import json
from random import randint
import re

class Random_French:
    
    def __init__(self):
        self.json = self.get_json()
            
    def get_json(self):
        with open('lang.json', 'rb') as f:
            data = json.load(f, encoding="utf-8")
        return data
    
    def random_verb(self):
        data = self.json['french_regular']
        output = {}
        while len(output) == 0:
            rand_num = randint(0, len(data)-1)
            verb = data[rand_num]
            tense = ['present', 'past', 'future'][randint(0,2)]
            rand_tense = verb[tense]
            eng_list = []
            #print(rand_tense)
            for key, val in rand_tense.items():
                eng_list.append(key)
            if eng_list == []:
                pass
            else:
                rand_eng = eng_list[randint(0, len(eng_list)-1)]
                output[rand_eng] = rand_tense[rand_eng]
            for key, val in output.items():
                if val == '':
                    output = {}
        return output
    
    def format_verb(self):
        output = self.random_verb()
        for key, val in output.items():
            english = key.split(',')
            french = val.split(',')
        langs = [english, french]
        question = langs[randint(0,1)]
        if question == english:
            correct_answer = french
        else:
            correct_answer = english
        if len(question) == 1:
            question = question[0]
        else:
            question = question[randint(0, len(question)-1)].lstrip()
        correct_answer = [l.lstrip() for l in correct_answer]
        return question, correct_answer


s = Random_French()


answer = ''
while answer != "stop":
    question, correct_answer = s.format_verb()
    answer = input('{}: '.format(question))
    if answer in correct_answer:
        print('Correct')
    else:
        print('Incorrect, the correct answer is: {}'.format(correct_answer))