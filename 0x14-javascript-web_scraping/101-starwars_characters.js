#!/usr/bin/node

const request = require('request');
const util = require('util');

const prequest = util.promisify(request);

if (process.argv.length !== 3) {
  console.error('Invalid number of arguments!');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

(async () => {
  try {
    const filmResponse = await prequest({ url, json: true });

    if (filmResponse && filmResponse.statusCode === 200) {
      const characters = filmResponse.body.characters;

      for (const charUrl of characters) {
        const charResponse = await prequest({ url: charUrl, json: true });

        if (charResponse && charResponse.statusCode === 200) {
          console.log(charResponse.body.name);
        } else {
          console.error(`Character request failed for URL: ${charUrl}`);
        }
      }
    } else {
      console.error('Film request failed.');
    }
  } catch (error) {
    console.error(error);
  }
})();
