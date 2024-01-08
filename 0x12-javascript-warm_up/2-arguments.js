#!/usr/bin/node

const i = process.argv.length;
console.log(i === 2 ? 'No argument' : i === 3 ? 'Argument found' : 'Arguments found');
