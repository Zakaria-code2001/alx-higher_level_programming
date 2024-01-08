#!/usr/local/bin/node

const num = Number(process.argv[2]);

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (!isNaN(num) && Number.isInteger(num) && num >= 0) {
  console.log(factorial(num));
} else {
  console.log('1');
}
