#!/usr/bin/node
/* Program to save into a new file an URL */

const fs = require('fs');
const { argv } = require('process');
const request = require('request');
const url = argv[2];
const nameOfFile = argv[3];

request(url, function (error, response, body) {
  if (error) console.log(error);
  fs.writeFile(nameOfFile, body, function (err) {
    if (err) throw err;
  })
});
