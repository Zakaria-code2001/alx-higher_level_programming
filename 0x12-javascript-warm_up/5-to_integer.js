#!/usr/bin/node

const inputs = process.argv;

const number = inputs[2];

if (number === undefined) {
  console.log('Not a number');
} else if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(number));
}
