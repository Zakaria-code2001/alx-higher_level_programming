#!/usr/bin/node

const inputs = process.argv;

const arg0 = inputs[2];

if (arg0 === undefined) {
  console.log('No argument');
} else if (arg0 !== undefined) {
  console.log(arg0);
}
