#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const inputs = process.argv;

const n1 = parseInt(inputs[2]);
const n2 = parseInt(inputs[3]);

console.log(add(n1, n2));
