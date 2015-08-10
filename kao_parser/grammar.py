from enum import Enum
from kao_decorators import lazy_property
import re

dependencyRegEx = re.compile("<[a-zA-Z]+>")

class Grammar(Enum):
    """ Represents the Grammar to use when parsing text """
        
    @lazy_property
    def regexString(self):
        """ Return the proper regex string """
        regexString = self.value
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
        results = dependencyRegEx.findall(self.value)
        return [result[1:-1] for result in results]
        
    def sibling(self, name):
        """ Return the sibling with the requested name """
        return self.__class__.__members__[name]