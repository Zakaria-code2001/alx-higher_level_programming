#!/usr/local/bin/node

const args = process.argv.slice(2).map(Number);
const nums = args.filter(num => !isNaN(num));

if (nums.length < 2) {
  console.log(0);
} else {
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}
