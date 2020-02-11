#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const info = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < info.length; i++) {
      if (info[i].characters.includes('https://swapi.co/api/people/' + '18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
