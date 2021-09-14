#!/usr/bin/node
/* Program to write a string to a file */

const args = process.argv;
const request = require('request');

request(args[2], function (error, response) {
  if (error) {
    console.error('error', error);
  } else {
    console.log('code: %d', response.statusCode);
  }
});
