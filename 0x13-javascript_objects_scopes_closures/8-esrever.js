#!/usr/bin/node

exports.esrever = function (list) {
    const reversedlist = []; 
    for (let i = -1; i < list.length; i--) {
        const valueAtIndex = list[i]
        reversedlist.push(valueAtIndex)
      }
      return reversedlist;
    }
    