from enum import Enum
from kao_decorators import lazy_property
import re

dependencyRegEx = re.compile("<[a-zA-Z]+>")

class Grammar(Enum):
    """ Represents the Grammar to use when parsing text """
    
    def __init__(self, value, token=str):
        """ Initialize with the value and token wrapper to use """
        self.regexWithDependencies = value
        self.token = token
        
    def match(self, text):
        """ Attempt to match the given text """
        match = self.regex.match(text)
        if match:
            return self.token(match.group(0))
        else:
            return None
        
    @lazy_property
    def regexString(self):
        """ Return the proper regex string """
        regexString = self.regexWithDependencies
        for dependency in self.dependencies:
            dependencySection = "<{0}>".format(dependency)
            dependencyRegEx = "({0})".format(self.sibling(dependency).regexString)
            regexString = regexString.replace(dependencySection, dependencyRegEx)
        return regexString
        
    @lazy_property
    def regex(self):
        """ Compile and return this regex """
        return re.compile(self.regexString)
        
    @lazy_property
    def dependencies(self):
        """ Return this rule's dependencies """
        results = dependencyRegEx.findall(self.regexWithDependencies)
        return [result[1:-1] for result in results]
        
    def sibling(self, name):
        """ Return the sibling with the requested name """
        return self.__class__.__members__[name]