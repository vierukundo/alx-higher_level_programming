#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer

if (process.argv.length !== 3) {
  console.error('Invalid number of arguments!');
  process.exit(1);
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const request = require('request');

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    console.log(body.title);
  } else {
    console.error('Request failed. Status code:', response.statusCode);
  }
});
