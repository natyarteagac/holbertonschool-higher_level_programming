#!/usr/bin/node
// Program to write a string to a file

const fs = require('fs');
const args = process.argv;

fs.writeFile(args[2], args[3], function (err) {
  if (err) {
    return console.log(err);
  }
});
