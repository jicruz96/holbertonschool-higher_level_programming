#!/usr/bin/env node
// Creates an exportable Rectangle class

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    let i, j;

    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }

  rotate () {
    const tmp = this.width;

    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
