#!/usr/bin/node

const args = process.argv.slice(2);
const number = Number(args[0]);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
