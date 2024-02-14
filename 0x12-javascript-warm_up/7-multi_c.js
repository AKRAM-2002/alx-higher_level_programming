#!/usr/bin/node

const args = process.argv.slice(2);
const x = args[0];
if (args.length === 0) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
  for (let i = 0; i < x; i++) console.log('C is fun');
}
