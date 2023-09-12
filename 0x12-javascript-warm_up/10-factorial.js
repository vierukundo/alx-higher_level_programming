#!/usr/bin/node

const num = Number(process.argv[2]);

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}

function factorial (n) {
  if (n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}
