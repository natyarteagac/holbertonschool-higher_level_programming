#!/usr/bin/node
/* Program to write a string to a file */

const { argv } = require('process');
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, function (error, response, body) {
  if (error) console.log(error);
  console.log(JSON.parse(body).title);
});
