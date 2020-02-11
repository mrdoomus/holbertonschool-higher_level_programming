#!/usr/bin/node
const request = require('request');

request('https://swapi.co/api/films/' + process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const info = JSON.parse(body);
    console.log(info.title);
  }
});
