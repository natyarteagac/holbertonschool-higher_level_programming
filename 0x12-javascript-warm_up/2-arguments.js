#!/usr/bin/node
/* Script to print if arguments exists or not
*/
const myVar = process.argv.length;

if (myVar < 3) {
  console.log('No argument');
} else if (myVar === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
