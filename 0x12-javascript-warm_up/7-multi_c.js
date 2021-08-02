#!/usr/bin/node
/* Loop to print all the array
*/

const x = process.argv[2];

if (!x) {
  console.log('Missing number of occurrences');
}
for (let index = 0; index < x; index++) {
  console.log('C is fun');
}
