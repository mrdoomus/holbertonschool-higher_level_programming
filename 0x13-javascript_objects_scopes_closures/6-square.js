#!/usr/bin/node
const Square1 = require('./5-square');

var square = class Square extends Square1 {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
module.exports = square;
