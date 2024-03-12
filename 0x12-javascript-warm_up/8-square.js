#!/usr/bin/node
const inputs = process.argv;

const n = inputs[2];

if (isNaN(n) || n === undefined) {
  console.log('Missing size');
}
for (let index = 0; index < n; index++) {
  console.log('X'.repeat(n));
}
