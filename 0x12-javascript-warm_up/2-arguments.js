#!/usr/local/bin/node
const argsCount = process.argv.length - 2;

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount > 0) {
  console.log('Argument found');
}
