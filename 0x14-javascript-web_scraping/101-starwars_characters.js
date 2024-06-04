#!/usr/bin/node
/*
 Write a script that prints all characters of a Star Wars movie:

 The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 Display one character name by line in the same order of the list “characters” in the /films/ response
 You must use the Star wars API
 You must use the module request
 */
const urlFilm = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

const req = require('request');
const array = [];

req.get(urlFilm, async (error, resp, body) => {
  if (!error && resp.statusCode === 200) {
    const data = JSON.parse(body);
    for (const urlChar of data.characters) {
      try {
        const charResponse = await getRequest(urlChar);
        const charData = JSON.parse(charResponse);
        array.push(charData.name);
      } catch (err) {
        console.error('Error:', err);
      }
    }
    for (let name = 0; name < array.length; name++) {
      console.log(array[name]);
    }
  }
});

function getRequest (url) {
  return new Promise((resolve, reject) => {
    req.get(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}
