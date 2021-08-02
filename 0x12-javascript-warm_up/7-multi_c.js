#!/usr/bin/node
/* Printing x times "C is fun".
*/

const x = process.argv[2];

if (!x) {
  console.log('Missing number of occurrences');
}
for (let index = 0; index < x; index++) {
  console.log('C is fun');
}
