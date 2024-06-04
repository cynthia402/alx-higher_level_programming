#!/usr/bin/node
/*
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request

*/

const url = process.argv[2];
const req = require('request');
let count = 0;
req(url, (error, respond, body) => {
  if (!error) {
    for (const data of JSON.parse(body).results) {
      for (const char of data.characters) {
        if (char.endsWith('18/')) {
          count += 1;
          break;
        }
      }
    }
    console.log(count);
  }
});
