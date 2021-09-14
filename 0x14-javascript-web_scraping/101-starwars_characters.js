#!/usr/bin/node
/* Program to write a string to a file */

const { argv } = require('process');
const request = require('request');
const movieId = argv[2];

request('https://swapi-api.hbtn.io/api/films', function (error, response, body) {
  if (error) console.log(error);
  const urlJson = JSON.parse(body).results;
  for (const movies of urlJson) {
    const characters = movies.characters;
    if (movieId === movies.episodeId) {
      for (let i = 0; i < characters.length; i++) {
        console.log(characters[i]);
      }
    }
  }
});
