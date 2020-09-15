#!/usr/bin/node

exports.callMeMoby = function (n, func) {
  let i;
  for (i = 0; i < n; i++) {
    func();
  }
};
