import re

class Parser:
    """ Represents a parser that can parse various strings and return the Tokenized results """
    
    def __init__(self, grammar):
        """ Initialize with the specific Grammar to try and match to """
        self.grammar = grammar
        
    def parse(self, text):
        """ Parse the given text """
        return self.grammar.match(text)