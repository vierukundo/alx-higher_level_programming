#!/usr/bin/node
// script that reads and prints the content of a file

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
