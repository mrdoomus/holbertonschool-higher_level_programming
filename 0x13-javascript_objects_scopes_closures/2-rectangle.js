#!/usr/bin/node
var rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
};
module.exports = rectangle;
