from kao_decorators import proxy_for
import re

dependencyRegEx = re.compile("<[a-zA-Z]+>")

class DependencyHelper:
    """ Helper class to handle loading the dependencies of a Grammar """
    
    def __init__(self, originalRegEx, GrammarCls):
        """ Initialize with the original regex string """
        self.originalRegEx = originalRegEx
        
        dependencyNames = self.extractDependencies()
        self.dependencies = [GrammarCls[name] for name in dependencyNames]
        self.dependencyMap = {name:GrammarCls[name] for name in dependencyNames}
        
    def extractDependencies(self):
        """ Return this rule's dependencies """
        results = dependencyRegEx.findall(self.originalRegEx)
        return [result[1:-1] for result in results]