#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}
if (process.argv.length < 4) {
  console.log('NaN');
} else {
  add(a, b);
}
