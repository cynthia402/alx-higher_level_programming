#!/usr/bin/node
/*
 Write a script that prints all characters of a Star Wars movie:

 The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 Display one character name by line
 You must use the Star wars API
 You must use the module request
 */

const urlFilm = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

const req = require('request');

req.get(urlFilm, (error, resp, body) => {
  if (!error && resp.statusCode === 200) {
    const data = JSON.parse(body);
    for (const urlChar of data.characters) {
      req.get(urlChar, (err, res, bodys) => {
        if (!err && res.statusCode === 200) {
          console.log(JSON.parse(bodys).name);
        }
      });
    }
  }
});
