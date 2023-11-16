#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      const square = c.repeat(this.width);
      for (let i = 0; i < this.height; ++i) {
        console.log(square);
      }
    }
  }
};
