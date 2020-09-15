#!/usr/bin/node
const numberOfArgs = process.argv.length - 2;

if (numberOfArgs) {
  if (numberOfArgs > 1) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
} else {
  console.log('No argument');
}
