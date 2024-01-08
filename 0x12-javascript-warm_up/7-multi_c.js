#!/usr/local/bin/node

const argv = process.argv[2];
const numArgv = Number(argv);

if (Number.isInteger(numArgv)) {
  for (let i = 0; i < numArgv; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
