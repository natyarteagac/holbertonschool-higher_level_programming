#!/usr/bin/node
/* Program to write a string to a file */

const args = process.argv;
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + args[2], function (error, body) {
  if (error) {
    console.error('code: %d', error);
  } else {
    console.log(JSON.parse(body.title));
  }
});
