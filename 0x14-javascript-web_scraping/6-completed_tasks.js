#!/usr/bin/node
/*
Write a script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module request
*/

const url = process.argv[2];
const req = require('request');
const dic = {};

req.get(url, (err, resp, body) => {
  if (!err && resp.statusCode === 200) {
    for (const data of JSON.parse(body)) {
      if (data.completed) {
        if (data.userId in dic) {
          dic[data.userId] += 1;
        } else {
          dic[data.userId] = 1;
        }
      }
    }
    console.log(dic);
  }
});
