#!/usr/bin/node

let nums = process.argv.slice(2);

if (nums.length < 2) {
  console.log(0);
} else {
  let max;
  let secondMax;
  const num1 = Number(nums[0]);
  const num2 = Number(nums[1]);
  let num;

  if (num1 < num2) {
    max = num2;
    secondMax = num1;
  } else {
    max = num1;
    secondMax = num2;
  }

  nums = nums.slice(2);
  for (num of nums) {
    if (num > secondMax) {
      if (num < max) {
        secondMax = num;
      } else {
        secondMax = max;
        max = num;
      }
    }
  }

  console.log(secondMax);
}
