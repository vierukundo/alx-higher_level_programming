#!/usr/bin/node

let secondBiggest = -Infinity; // Initialize to negative infinity
let max = -Infinity; // Initialize to negative infinity

if (!process.argv[2] || process.argv.length === 3) {
  console.log(0);
} else {
  console.log(secondBiggestNum(process.argv));
}

function secondBiggestNum (nums) {
  for (let i = 2; i < nums.length; i++) {
    if (Number(nums[i]) > max) {
      secondBiggest = max; // Update secondBiggest before updating max
      max = Number(nums[i]);
    } else if (Number(nums[i]) > secondBiggest && Number(nums[i]) !== max) {
      secondBiggest = Number(nums[i]);
    }
  }
  return secondBiggest;
}
