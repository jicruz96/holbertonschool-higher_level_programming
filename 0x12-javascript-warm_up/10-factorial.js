#!/usr/bin/node

let num = Number(process.argv[2]);

function factorial (n) {
  if (n < 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

if (isNaN(num)) {
  num = 1;
}

console.log(factorial(num));
