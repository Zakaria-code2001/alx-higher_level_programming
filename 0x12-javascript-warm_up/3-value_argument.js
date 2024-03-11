#!/usr/bin/node

const inputs = process.argv;

const arg0 = inputs[2];
const arg1 = inputs[3];

if (arg0 === undefined) {
  console.log('No argument');
} else if (arg0 != undefined) {
  console.log(arg0);
}
