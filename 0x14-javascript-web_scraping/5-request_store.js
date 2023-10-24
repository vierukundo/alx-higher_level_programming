#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

if (process.argv.length !== 4) {
  console.error('Invalid arguments!');
  process.exit(1);
}

const filePath = process.argv[3];
const url = process.argv[2];

const fs = require('fs');
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.error('Request failed. Status code:', response.statusCode);
  }
});
