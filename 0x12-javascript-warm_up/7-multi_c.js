#!/usr/bin/node

const argv = process.argv[2];
const x = Number(argv);

if (Number.isInteger(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
