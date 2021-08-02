#!/usr/bin/node
/* Script to check if argument giving is int.
*/

const myVar = process.argv;

if (parseInt(myVar[2])) {
  console.log('My number: ' + myVar[2]);
} else {
  console.log('Not a number');
}
