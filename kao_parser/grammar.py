from .dependency_helper import DependencyHelper
from .regex_helper import RegexHelper
from .token_builder import TokenBuilder
from .leaf_token_builder import LeafTokenBuilder

from enum import Enum
from kao_decorators import proxy_for

@proxy_for("dependencyHelper", ["numberOfGroups", "dependencies"])
@proxy_for("regexHelper", ["regex", "regexString"])
@proxy_for("builder", ["buildFromMatch", "build"])
class Grammar(Enum):
    """ Represents the Grammar to use when parsing text """
    
    def __init__(self, originalRegEx, token=None):
        """ Initialize with the value and token wrapper to use """
        self.dependencyHelper = DependencyHelper(originalRegEx, self.__class__)
        self.regexHelper = RegexHelper(originalRegEx, self.dependencyHelper)
        
        if len(self.dependencies) > 0:
            self.builder = TokenBuilder(self.dependencyHelper, token)
        else:
            self.builder = LeafTokenBuilder(self.dependencyHelper, token)
        
    def match(self, text):
        """ Attempt to match the given text """
        match = self.regex.match(text)
        
        if match:
            return self.buildFromMatch(match)
        else:
            return None