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

class App:
    
    def __init__(self):
        pass
    
    def get_json(self):
        with open('lang.json') as f:
            data = json.load(f)
        return data
    
    def random_verb(self):
        verbs = self.get_json()["french_regular"]
        random_num = randint(0, len(verbs))
        rand_verb = verbs[random_num]
        return rand_verb
    
    def conjugate(self):
        verb = self.random_verb()
    
    def generate(self):
        pass
    

