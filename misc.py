class NoCodeSupplied(Exception):
    pass

class NoImportPath(Exception):
    pass

class UnderscoreNotPermitted(Exception):
    pass

class NoArgumentsSupplied(Exception):
    pass

def replaceSpacesWithUnderscores(string):
    # Replace the spaces in string with underscores
    # If the string already contains underscores, raise an error

    if '_' in string:
        raise UnderscoreNotPermitted
    else:
        return string.replace(' ', '_')