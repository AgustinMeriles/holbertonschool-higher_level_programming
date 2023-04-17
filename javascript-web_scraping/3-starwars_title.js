#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get({ url }, (error, response, data) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(data);
    console.log(movie.title);
  }
});
