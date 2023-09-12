#!/usr/bin/node

let i = Number(process.argv[2]);
if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
