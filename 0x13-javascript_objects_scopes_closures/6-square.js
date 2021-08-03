#!/usr/bin/node
/* Define the Square class
*/

class Square extends require('./5-square') {
  // Define Square class
  constructor (size) {
    // Calling rectangle's attributes.
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    // Print the size of Square and verify if variable exists print with the character C if not print with X
    for (let index = 0; index < this.size; index++) {
      if (!c) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
