from kao_decorators import proxy_for

@proxy_for("dependencyHelper", ["numberOfGroups", "dependencies"])
class LeafTokenBuilder:
    """ Helper class to build a leaf token """
    
    def __init__(self, dependencyHelper, token):
        """ Initialize the Token Builder """
        self.dependencyHelper = dependencyHelper
        self.token = str if token is None else token
        
    def buildFromMatch(self, match):
        """ Build from the given match """
        return self.build(match.group())
        
    def build(self, value):
        """ Build the token from the value """
        if value is not None:
            return self.token(value)
        else:
            return None