#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  }
  const result = n * factorial(n - 1);
  if (!isFinite(result)) {
    return Infinity;
  }
  return result;
}

const number = parseInt(process.argv[2]);

console.log(factorial(number));
