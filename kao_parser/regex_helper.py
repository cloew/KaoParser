from kao_decorators import lazy_property
import re

class RegexHelper:
    """ Helper class to cleanup usage of the regex string """
    
    def __init__(self, originalRegEx, dependencyHelper):
        """ Initialize the Helper with the string """
        self.originalRegEx = originalRegEx
        self.dependencyHelper = dependencyHelper
    
    @lazy_property
    def regexString(self):
        """ Return the proper regex string """
        regexString = self.originalRegEx
        for dependency in self.dependencyHelper.dependencyMap:
            dependencySection = "<{0}>".format(dependency)
            dependencyRegEx = "({0})".format(self.dependencyHelper.dependencyMap[dependency].regexString)
            regexString = regexString.replace(dependencySection, dependencyRegEx)
        return regexString
        
    @lazy_property
    def regex(self):
        """ Compile and return this regex """
        return re.compile(self.regexString)