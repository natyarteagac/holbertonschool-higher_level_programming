#!/usr/bin/node
/* Function that converst a number from base 10 to another
base paased as argument
*/

exports.converter = function (base) {
  return function (x) {
    return x.toString(base);
  };
};
