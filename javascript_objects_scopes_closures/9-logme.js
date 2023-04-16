#!/usr/bin/node
let cont = 0;
exports.logMe = function (item) {
  cont += 1;
  if (item) {
    console.log(`${cont}: ${item}`);
  }
};
