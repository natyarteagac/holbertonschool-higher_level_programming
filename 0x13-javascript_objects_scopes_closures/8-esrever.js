#!/usr/bin/node
/* Function to return the reversed version of a list
*/

exports.esrever = function (list) {
  const newList = [];
  let count = list.length - 1;
  while (count >= 0) {
    newList.push(list[count]);
    count--;
  }
  return newList;
};
