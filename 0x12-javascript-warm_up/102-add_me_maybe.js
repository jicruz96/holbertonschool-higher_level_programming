#!/usr/bin/node

exports.addMeMaybe = function (Me, func) {
  Me++;
  func(Me);
};
