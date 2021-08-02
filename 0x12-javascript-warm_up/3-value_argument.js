#!/usr/bin/node
/* Script to print if arguments exists or not
*/
const myVar = process.argv;

if (!myVar[2]) {
  console.log('No argument');
} else if (myVar[2]) {
  console.log(myVar[2]);
}
