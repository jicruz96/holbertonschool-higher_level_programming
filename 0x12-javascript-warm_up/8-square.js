#!/usr/bin/node

const size = Number(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let str = '';
  let i;

  for (i = 0; i < size; i++) {
    str += 'X';
  }

  for (i = 0; i < size; i++) {
    console.log(str);
  }
}
