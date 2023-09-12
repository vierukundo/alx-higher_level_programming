#!/usr/bin/node

const n = Number(process.argv[2]);
const side = [];

if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else if (n > 0){
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      side.push('X');
    }
    console.log(side.join(''));
    side.length = 0; // Clear the array
  }
}
