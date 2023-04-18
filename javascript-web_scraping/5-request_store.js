#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get({ url }, 'utf-8', (error, response, data) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, data, (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
