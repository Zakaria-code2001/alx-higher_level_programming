#!/usr/bin/node

const x = Number(process.argv[2]);
const y = Number(process.argv[3]);

if (!isNaN(x) && !isNaN(y) && Number.isInteger(x) && Number.isInteger(y)) {
  console.log(x + y);
} else {
  console.log('NaN');
}
