from kao_decorators import proxy_for

@proxy_for("dependencyHelper", ["numberOfGroups", "dependencies"])
class TokenBuilder:
    """ Helper class to build the token """
    
    def __init__(self, dependencyHelper, token):
        """ Initialize the Token Builder """
        self.dependencyHelper = dependencyHelper
        self.token = token
        
    def buildFromMatch(self, match):
        """ Build from the given match """
        return self.build(match.groups())
        
    def build(self, groups):
        """ Build the token from the groups """
        next = 0
        tokens = []
        for dependency in self.dependencies:
            next += 1
            end = next+dependency.numberOfGroups
            token = None
            
            if dependency.numberOfGroups > 0:
                token = dependency.build(groups[next:end])
            else:
                token = dependency.build(groups[next-1])
        
            if token is not None:
                tokens.append(token)
            next = end
            
        if len(tokens) == 0:
            return None
        else:
            return self.token(*tokens)