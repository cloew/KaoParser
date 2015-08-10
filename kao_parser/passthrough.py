
def Passthrough(*args):
    """ A method that returns the argument list or the only value """
    if len(args) == 1:
        return args[0]
    else:
        return args