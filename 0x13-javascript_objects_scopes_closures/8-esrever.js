#!/usr/bin/node
// Reverse!

exports.esrever = function (list) {
  const tsil = [];
  let i = 0;

  for (i = 0; i < list.length; i++) {
    // tsil.push(list[i]);
    tsil.unshift(list[i]);
  }
  return tsil;
};
