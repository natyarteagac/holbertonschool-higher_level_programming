#!/usr/bin/node
/* Program to write a string to a file */

const { argv } = require('process');
const request = require('request');
const url = argv[2];
let counter = 0;

request(url, function (error, response, body) {
  if (error) console.log(error);
  const urlJson = JSON.parse(body).results;
  for (const movies of urlJson) {
    const characters = movies.characters;
    for (const oneChar of characters) {
      if (oneChar.endsWith('18/') === true) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
