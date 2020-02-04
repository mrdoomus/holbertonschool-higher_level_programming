#!/usr/bin/node

function factorial (n) {
  const num = parseInt(Number(n));
  if (isNaN(num) || num === 1) {
    return 1;
  }
  return n * factorial(num - 1);
}

console.log(factorial(process.argv[2]));
