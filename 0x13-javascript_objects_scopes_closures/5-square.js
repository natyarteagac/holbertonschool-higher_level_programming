#!/usr/bin/node
/* Define the Square class
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  // Define size attribute of Square
  constructor (size) {
    // Calling rectangle's attributes.
    super(size, size);
  }
}
module.exports = Square;
