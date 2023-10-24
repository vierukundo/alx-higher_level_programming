#!/usr/bin/node
// script that writes a string to a file.

if (process.argv.length !== 4) {
  console.error('Invalid arguments!');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

const fs = require('fs');

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
