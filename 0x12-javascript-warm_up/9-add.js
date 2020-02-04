#!/usr/bin/node

function add (a, b) {
  const num1 = parseInt(Number(a));
  const num2 = parseInt(Number(b));
  if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
  } else {
    console.log(num1 + num2);
  }
}

add(process.argv[2], process.argv[3]);
