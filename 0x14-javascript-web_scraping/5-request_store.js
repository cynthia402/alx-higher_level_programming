#!/usr/bin/node
/*
Write a script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module request
*/
const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const path = process.argv[3];

req.get(url, (error, respond, body) => {
  if (!error && respond.statusCode === 200) {
    fs.writeFile(path, body, 'utf-8', (err, resp) => {
      if (!err && resp) {
        console.log(resp.statusCode);
      }
    });
  }
});
