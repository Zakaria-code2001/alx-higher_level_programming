#!/usr/bin/node

const c = 'C is fun';
const inputs = process.argv;

const nOfTimes = inputs[2];

if (isNaN(nOfTimes) || nOfTimes === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < nOfTimes; index++) {
    console.log(c);
  }
}
