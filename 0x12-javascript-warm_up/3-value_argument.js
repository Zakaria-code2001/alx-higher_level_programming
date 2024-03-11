#!/usr/bin/node

const inputs = process.argv;

const argsCount = process.argv.length - 2;
const arg1 = inputs[2];

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log(arg1);
}
