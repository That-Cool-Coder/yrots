
// Main function in case the main function is not overwritten
function main() {}

// Sleep function to make node more synchronious
function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}   



async function main() {
console.log('Test 1');
await sleep(1000);
console.log('Test 2');
}


// Driver code
main(...process.argv);
