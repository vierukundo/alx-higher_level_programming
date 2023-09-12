#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const width = [];
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        width.push('X');
      }
      console.log(width.join(''));
      width.length = 0;
    }
  }
}

module.exports = Rectangle;
