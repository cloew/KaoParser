from .regex_helper import RegexHelper

from enum import Enum
from kao_decorators import lazy_property, proxy_for
import re

dependencyRegEx = re.compile("<[a-zA-Z]+>")

@proxy_for("regexHelper", ["regex"])
class Grammar(Enum):
    """ Represents the Grammar to use when parsing text """
    
    def __init__(self, value, token=str):
        """ Initialize with the value and token wrapper to use """
        self.regexHelper = RegexHelper(value, self)
        self.token = token
        
    def match(self, text):
        """ Attempt to match the given text """
        match = self.regex.match(text)
        if match:
            return self.token(match.group(0))
        else:
            return None
        
    @lazy_property
    def dependencies(self):
        """ Return this rule's dependencies """
        results = dependencyRegEx.findall(self.regexHelper.originalRegEx)
        return [result[1:-1] for result in results]
        
    def sibling(self, name):
        """ Return the sibling with the requested name """
        return self.__class__.__members__[name]