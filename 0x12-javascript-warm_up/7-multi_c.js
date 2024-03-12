#!/usr/bin/node

const c = 'C is fun';
const inputs = process.argv;

const n_of_times = inputs[2];

if (isNaN(n_of_times) || n_of_times === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < n_of_times; index++) {
    console.log(c);
  }
}
