#!/usr/bin/node

if (Number.isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${process.argv[2]}`);
}
