
// Main function in case the main function is not overwritten
function main() {}



function Hello_2(weather) {
console.log('The arg passed to hello 2 is:');
console.log(weather);
}



function main(pancakes, dogs, flies) {
console.log('Test print function');
Hello_2(flies);
A_Desolate_Desert();
dog = 9;
console.log('The value of dog is:');
console.log(dog);
}

function A_Desolate_Desert() {
console.log('Test function call');
}


// Driver code
main(...process.argv);
