import string
from misc import *

# Main function
# -------------

def compileLine(yrotsLine):
    # split into words by white space
    words = yrotsLine.split()
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    words = [w.translate(table) for w in words]

    keyword = words[1]

    if keyword in LINE_KEYWORDS:
        func = LINE_KEYWORDS[keyword]
        return func(yrotsLine, words)
    else:
        return ''

# Command compilers
# (prefixed with cmd_ for clarity)
# --------------------------------

def cmd_print(yrotsLine, words):
    if words[2] == 'that':
        # Get the variable name
        toPrint = words[3]
        # and print it
        compiledLine = f'''console.log({toPrint});\n'''
    else:
        # Get the text inside the quotes
        toPrint = yrotsLine.split('"')[1]
        # and print it
        compiledLine = f'''console.log('{toPrint}');\n'''
    return compiledLine

def cmd_functionCall(yrotsLine, words):
    functionNameStartIdx = words.index('called') + 1
    argumentsStartIndex = words.index('about') + 1

    functionName = '_'.join(words[functionNameStartIdx:
        argumentsStartIndex - 1])
    
    arguments = ', '.join(words[argumentsStartIndex:])

    return f'''{functionName}({arguments});\n'''

def cmd_varSet(yrotsLine, words):
    if 'was' in words:
        keywordIndex = words.index('was')
    else:
        keywordIndex = words.index('is')
    varName = words[keywordIndex - 1]
    value = words[keywordIndex + 1]

    return f'{varName} = {value};\n'

def cmd_sleep(yrotsLine, words):
    secondsToSleep = int(words[3])
    msToSleep = secondsToSleep * 1000
    return f'await sleep({msToSleep});\n'


LINE_KEYWORDS = {
    'said' : cmd_print,
    'yelled' : cmd_print,
    'argued' : cmd_print,
    'replied' : cmd_print,
    'protested' : cmd_print,
    'cried' : cmd_print,
    'stated' : cmd_print,
    
    'read' : cmd_functionCall,

    'is' : cmd_varSet,
    'was' : cmd_varSet,

    'slept' : cmd_sleep
}