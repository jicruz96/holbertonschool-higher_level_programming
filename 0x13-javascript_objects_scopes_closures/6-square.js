#!/usr/bin/node

const Space = require('./5-square');

module.exports = class Square extends Space {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    this.print(c);
  }
};
