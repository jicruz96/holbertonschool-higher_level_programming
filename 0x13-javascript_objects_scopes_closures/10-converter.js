#!/usr/bin/node
// converts

exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
