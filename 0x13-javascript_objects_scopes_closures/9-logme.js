#!/usr/bin/node
/* Function that prints the number of arguments already
printed and the new argument value
*/
let myVar = 0;

exports.logMe = function (item) {
  console.log(myVar + ': ' + item);
  myVar += 1;
};
