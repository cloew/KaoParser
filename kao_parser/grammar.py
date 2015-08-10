from .dependency_helper import DependencyHelper
from .regex_helper import RegexHelper

from enum import Enum
from kao_decorators import lazy_property, proxy_for

@proxy_for("regexHelper", ["regex"])
class Grammar(Enum):
    """ Represents the Grammar to use when parsing text """
    
    def __init__(self, originalRegEx, token=str):
        """ Initialize with the value and token wrapper to use """
        self.dependencyHelper = DependencyHelper(originalRegEx, self.__class__)
        self.regexHelper = RegexHelper(originalRegEx, self.dependencyHelper)
        self.token = token
        
    def match(self, text):
        """ Attempt to match the given text """
        match = self.regex.match(text)
        if match:
            return self.token(match.group(0))
        else:
            return None