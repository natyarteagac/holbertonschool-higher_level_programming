#!/usr/bin/node
/* Defining instance attributes w and h for Rectangle class
*/

class Rectangle {
  // Defining width and height attributes.
  constructor (w, h) {
    // if w and h are bigger than 0 --> define the instance attribute.
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Instance function to print the height and the width of rectangle.
    for (let index = 0; index < this.height; index++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Interchanges the value of width with height.
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    // Multiplies the width and the height by two.
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
