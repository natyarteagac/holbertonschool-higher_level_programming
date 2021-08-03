#!/usr/bin/node
/* Defining instance attributes w and h for Rectangle class
*/

class Rectangle {
  // Defining width and height attributes.
  constructor (w, h) {
    // if width and height are bigger --> define the instance attribute.
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
