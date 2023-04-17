#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get({ url }, (error, response, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
