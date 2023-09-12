#!/usr/bin/node

const n = Number(process.argv[2]);
let side = '';
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      side += 'X';
    }
    console.log(`${side}`);
    side = '';
  }
}
