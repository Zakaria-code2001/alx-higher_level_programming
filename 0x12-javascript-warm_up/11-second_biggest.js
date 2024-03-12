#!/usr/bin/node
const nums = [];

for (let i = 2; i < process.argv.length; i++) {
  nums.push(process.argv[i]);
}

nums.sort();
const secondBigger = nums[nums.length - 2];
if (isNaN(secondBigger) || secondBigger === undefined) {
  console.log(0);
} else { console.log(secondBigger); }
