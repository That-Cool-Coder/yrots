from misc import *
from lineCompiler import compileLine

SUBLINE_SPLITTER = '.'
LINE_SPLITTER = '\n\n' # one empty line

CHAPTER_NUM_SPLITTER = ':' # splits the chapter num from the function name

ARGUMENTS_FLAG = 'A tale of'
NO_ARGUMENTS_FLAG = 'A tale to tell'

def compileFunction(yrotsFunction, isEntryPoint):
    yrotsLines = yrotsFunction.split(LINE_SPLITTER)
    yrotsFunctionHeader = yrotsLines.pop(0)

    functionName = compileFunctionName(yrotsFunctionHeader)
    arguments = compileArguments(yrotsFunctionHeader)

    if functionName == 'Introduction':
        # If this is the main file, and the main function should run,
        # rename it then continue compiling
        if isEntryPoint:
            functionName = 'main'
        # Otherwise, we don't care about this function and we should get rid of item
        else:
            return ''

    compiledFunctionHeader = \
        f'function {functionName}({arguments}) {{\n'
    
    compiledFunction = compiledFunctionHeader
    for yrotLine in yrotsLines:
        compiledFunction += compileLine(yrotLine)

    compiledFunction += '}\n\n'

    return compiledFunction

def compileFunctionName(yrotsFunctionHeader):
    # Return a string of the function name

    functionName = yrotsFunctionHeader.split('\n')[0]
    functionName = functionName.split(CHAPTER_NUM_SPLITTER)[1]
    functionName = functionName.strip()
    functionName = replaceSpacesWithUnderscores(functionName);
    return functionName

def compileArguments(yrotsFunctionHeader):
    # Return a string of the input vars seperated by commas

    argumentsStr = yrotsFunctionHeader.split('\n')[1]

    # If there is a flag saying no input vars, then return empty string as there are no args
    if NO_ARGUMENTS_FLAG in argumentsStr:
        return ''

    # If there are no arguments and there is nothing stating the lack of arguments,
    # then raise an error
    if (not ARGUMENTS_FLAG in argumentsStr) and \
        (not NO_ARGUMENTS_FLAG in argumentsStr):

        raise NoArgumentsSupplied

    argumentsStr = argumentsStr.replace(ARGUMENTS_FLAG, '', 1)
    argumentsStr = argumentsStr.strip()

    # If there are 3 or more
    if ',' in argumentsStr:
        arguments = argumentsStr.split(',')

        # split the last two items
        lastTwoVars = arguments.pop().split('and')
        arguments.append(lastTwoVars[0])
        arguments.append(lastTwoVars[1])

    # If there are just two
    elif 'and' in argumentsStr:
        arguments = argumentsStr.split('and')

    # If there is just one
    else:
        arguments = [argumentsStr]
    
    compiledArguments = ''
    for argument in arguments:
        argument = argument.strip()
        argument = replaceSpacesWithUnderscores(argument)
        compiledArguments += argument + ', '

    # Remove the last ', '
    compiledArguments = compiledArguments[:-2]

    return compiledArguments