#!/usr/bin/node

const args = process.argv.slice(2);

function add (a, b) {
  return parseInt(a, 10) + parseInt(b, 10);
}

if (args.length === 2) {
  const result = add(args[0], args[1]);
  if (!Number.isNaN(result)) {
    console.log(result);
  } else {
    console.log('NaN');
  }
} else {
  console.log('NaN');
}
