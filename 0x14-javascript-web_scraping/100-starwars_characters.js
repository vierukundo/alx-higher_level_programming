#!/usr/bin/node
// script that prints all characters of a Star Wars movie

if (process.argv.length !== 3) {
  console.error('Invalid number of arguments!');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`; // Fix the URL formatting
const request = require('request');

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const charactersUrls = body.characters;

    // Use a loop to request and print character names
    charactersUrls.forEach((charUrl) => {
      request(charUrl, { json: true }, (error, response, charBody) => {
        if (error) {
          console.error(error);
          return;
        }
        console.log(charBody.name);
      });
    });
  } else {
    console.error('Request failed. Status code:', response.statusCode);
  }
});
