# These are headers to include in the compiler js

PRE_CODE_HEADER = \
'''
// Main function in case the main function is not overwritten
function main() {}

// Sleep function to make node more synchronious
function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}   


'''

POST_CODE_FOOTER = \
'''
// Driver code
main(...process.argv);
'''