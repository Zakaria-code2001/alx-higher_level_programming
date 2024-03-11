#!/usr/local/bin/node
const argsCount = process.argv.length - 2;

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else if (argsCount > 1) {
  console.log('Arguments found');
}
