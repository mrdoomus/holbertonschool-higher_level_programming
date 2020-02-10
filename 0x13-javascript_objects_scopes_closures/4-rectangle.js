#!/usr/bin/node
var rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }

  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  };

  this.rotate = function () {
    const heightHolder = this.height;
    this.height = this.width;
    this.width = heightHolder;
  };

  this.double = function () {
    this.height *= 2;
    this.width *= 2;
  };
};
module.exports = rectangle;
