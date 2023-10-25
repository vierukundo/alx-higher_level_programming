#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present

if (process.argv.length !== 3) {
  console.error('Invalid number of arguments!');
  process.exit(1);
}

const url = process.argv[2];
const request = require('request');

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movies = body.results;
    let numOfMovies = 0;

    for (const movie of movies) {
      const characters = movie.characters;
      for (const characterUrl of characters) {
        if (characterUrl.includes('18')) {
          numOfMovies++;
        }
      }
    }

    console.log(numOfMovies);
  }
});
