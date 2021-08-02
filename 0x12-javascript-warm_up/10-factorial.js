#!/usr/bin/node
/* Function to print the result of the factorial
*/

function factorial (a) {
  if (!a) {
    return 1;
  }
  return a * factorial(a - 1);
}
const myVar = parseInt(process.argv[2]);
console.log(factorial(myVar));
