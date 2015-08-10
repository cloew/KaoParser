from enum import Enum
from kao_decorators import lazy_property
import re

class Grammar(Enum):
    """ Represents the Grammar to use when parsing text """
        
    @lazy_property
    def regex(self):
        """ Compile and return this regex """
        return re.compile(self.value)