#!/usr/bin/node

let count = 0;
exports.logMe = function (item) {
  for (let items = 0; items < item.length; items++) {
    console.log(`${count}: ${item} `);
    count++;
  }
};
