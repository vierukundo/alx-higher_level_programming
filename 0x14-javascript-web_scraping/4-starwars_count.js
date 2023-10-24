#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present

if (process.argv.length !== 3) {
  console.error('Invalid number of arguments!');
  process.exit(1);
}

const url = process.argv[2];
const wedgeAntillesURL = 'https://swapi-api.alx-tools.com/api/people/18/';
const request = require('request');

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movies = body.results;
    let numOfMovies = 0;

    // Iterate through the movies and check if Wedge Antilles is present
    for (const movie of movies) {
      if (movie.characters.includes(wedgeAntillesURL)) {
        numOfMovies++;
      }
    }

    console.log(numOfMovies);
  }
});
