import sys
import os.path
from misc import *
from functionCompiler import compileFunction
from compiledHeaders import *

FUNCTION_SPLITTER = '\n\n\n\n' # three empty lines

NO_IMPORT_FLAG = 'This is the first book by this author'
IMPORT_FOLDER_FLAG = 'from the series'

DEBUG_MODE_FLAG = 'debug'

def compileYrots(inputFileName=None, outputFileName=None, yrotsCode=None,
    compileFlags=[], isEntryPoint=True):
    # isEntryPoint defines whether this is the 'main' file that is being compiled.
    # if this is false, then this file is being compiled as an imported
    # don't specify isEntryPoint if you are calling this from another project

    # If you leave inputFileName as None then this will try to use yrotsCode as input
    # If you leave outputFileName as None then this will return the compiled code

    print('Compiling', inputFileName)

    # If no input code was supplied, raise an error
    if inputFileName is None and yrotsCode is None:
        raise NoCodeSupplied

    # If an input file was specified, read it
    if inputFileName is not None:
        # let it crash if the file is not found
        inputFile = open(inputFileName, 'r', encoding='utf-8')
        yrotsCode = inputFile.read()
        inputFile.close()

    programName, yrotsImports, yrotsFunctionList = splitMainSections(yrotsCode)

    compiledCode = ''

    # If debug mode is on, then put some debug info
    if DEBUG_MODE_FLAG in compileFlags and inputFile is not None:
        compiledCode += f'// Start of compiled code from {inputFileName}\n'

    # If this is the main file,
    # then add the header
    if isEntryPoint:
        compiledCode += PRE_CODE_HEADER

    compiledCode += compileImports(yrotsImports, compileFlags) + '\n'
    compiledCode += compileBody(yrotsFunctionList, compileFlags, isEntryPoint)
    
    # If this is the main file,
    # then add the footer
    if isEntryPoint:
        compiledCode += POST_CODE_FOOTER

    # If debug mode is on, then put some debug info
    if DEBUG_MODE_FLAG in compileFlags and inputFile is not None:
        compiledCode += f'// End of compiled code from {inputFileName}\n'

    print('Done compiling', inputFileName)

    # If an output file was specified, write to it
    if outputFileName is not None:
        outputFile = open(outputFileName, 'w+', encoding='utf-8')
        outputFile.write(compiledCode)
        outputFile.close()
    # Else just return the code
    else:
        return compiledCode

def splitMainSections(code):
    sections = code.split(FUNCTION_SPLITTER)
    programName, yrotsImports = tuple(sections[:2])
    
    yrotsFunctionList = sections[2:]

    return (programName, yrotsImports, yrotsFunctionList)

def compileImports(yrotsImports, compileFlags):
    compiledImports = ''
    importDataList = yrotsImports.split('\n')
    if importDataList[0] == NO_IMPORT_FLAG:
        return ''
    else:
        importDataList.pop(0) # remove heading
        for importData in importDataList:
            path = getImportPath(importData)

            compiledImports += compileYrots(inputFileName=path, compileFlags=compileFlags, isEntryPoint=False) + '\n'
        return compiledImports

def getImportPath(importData):
    importData = importData.strip()
    importData = importData[2:] # remove ' - ' at start

    importDataSections = importData.split('(')

    fileName = importDataSections[0].strip()
    directory = ''

    if len(importDataSections) > 1:
        directoryInfo = importDataSections[1].strip()
        directoryInfo = directoryInfo[:-1] # remove closing bracket
        directoryInfo = directoryInfo.replace(IMPORT_FOLDER_FLAG, '', 1)
        directory = directoryInfo.strip()
    else:
        directoryInfo = ''

    return directory + '/' + fileName + '.yrot'

def compileBody(yrotsFunctionList, compileFlags, isEntryPoint):
    compiledBody = ''
    for yrotsFunction in yrotsFunctionList:
        compiledBody += compileFunction(yrotsFunction.strip(), isEntryPoint)
    return compiledBody

if __name__ == '__main__':
    compileFlags = []
    if len(sys.argv) >= 4:
        compileFlags = sys.argv[3:]
    compileYrots(inputFileName=sys.argv[1], outputFileName=sys.argv[2], compileFlags=compileFlags)