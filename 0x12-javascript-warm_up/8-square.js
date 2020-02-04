#!/usr/bin/node

const j = parseInt(process.argv[2]);

if (isNaN(j)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < j; i++) {
    console.log('X'.repeat(j));
  }
}
