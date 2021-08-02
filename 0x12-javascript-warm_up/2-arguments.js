#!/usr/bin/node
/* Script to print if arguments exists or no
*/

if (!process.argv[2]) {
  console.log('No argument');
} else if (process.argv.length[3] === process.argv[3]) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
