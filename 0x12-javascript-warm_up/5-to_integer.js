#!/usr/bin/node

const argv = process.argv[2];
const numArgv = Number(argv);

if (Number.isInteger(numArgv)) {
  console.log(`My number: ${numArgv}`);
} else {
  console.log('Not a number');
}
