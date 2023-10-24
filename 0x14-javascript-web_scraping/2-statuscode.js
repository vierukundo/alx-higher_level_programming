#!/usr/bin/node
// script that display the status code of a GET request

if (process.argv.length !== 3) {
  console.error('Invalid arguments');
  process.exit(1);
}

const url = process.argv[2];

const request = require('request');

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
