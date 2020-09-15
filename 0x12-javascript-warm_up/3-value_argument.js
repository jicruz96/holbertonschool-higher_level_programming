#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0]) {
  let arg;
  for (arg of args) {
    console.log(arg);
  }
} else {
  console.log('No argument');
}
