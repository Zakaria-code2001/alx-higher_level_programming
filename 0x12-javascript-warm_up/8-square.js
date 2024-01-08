#!/usr/bin/node

const argv = process.argv[2];
const size = Number(argv);
const x = 'X';

if (!Number.isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log(x.repeat(size));
  }
} else {
  console.log('Missing size');
}
