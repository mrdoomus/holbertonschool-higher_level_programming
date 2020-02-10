#!/usr/bin/node
const Rectangle = require('./4-rectangle');

var square = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
module.exports = square;
