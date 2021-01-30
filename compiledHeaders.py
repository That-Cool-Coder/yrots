# These are headers to include in the compiler js

PRE_CODE_HEADER = \
'''
// Main function in case the main function is not overwritten
function main() {}


'''

POST_CODE_FOOTER = \
'''
// Driver code
main(...process.argv);
'''