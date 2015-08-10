from .dependency_helper import DependencyHelper
from .regex_helper import RegexHelper

from enum import Enum
from kao_decorators import proxy_for

@proxy_for("dependencyHelper", ["numberOfGroups", "dependencies"])
@proxy_for("regexHelper", ["regex", "regexString"])
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
            if len(self.dependencies) > 0:
                return self.buildToken(match.groups())
            else:
                return self.buildLeafToken(match.group())
        else:
            return None
            
    def buildToken(self, groups):
        """ Build token from the groups """
        next = 0
        tokens = []
        for dependency in self.dependencies:
            next += 1
            end = next+dependency.numberOfGroups
            token = None
            
            if dependency.numberOfGroups > 0:
                token = dependency.buildToken(groups[next:end])
            else:
                token = dependency.buildLeafToken(groups[next-1])
        
            tokens.append(token)
            next = end
        return self.token(tokens)
            
    def buildLeafToken(self, value):
        """ Return the value of the Leaf Token """
        if value is not None:
            return self.token(value)
        else:
            return None