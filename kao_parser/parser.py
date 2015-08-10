import re

class Parser:
    """ Represents a parser that can parse various strings and return the Tokenized results """
    
    def __init__(self, word):
        """ Initialize with the Word to try and match to """
        self.word = word
        
    def parse(self, text):
        """ Parse the given text """
        return self.word.regex.match(text)