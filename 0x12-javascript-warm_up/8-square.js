#!/usr/bin/node
/* Function to print a square with giving argv
*/

const size = parseInt(process.argv[2]);

if (!size) {
  console.log('Missing size');
}
for (let index = 0; index < size; index++) {
  console.log('X'.repeat(size));
}
