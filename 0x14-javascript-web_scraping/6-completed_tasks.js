#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const dictTasks = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0,
      6: 0,
      7: 0,
      8: 0,
      9: 0,
      10: 0
    };
    const tasks = JSON.parse(body);
    tasks.forEach(function (task) {
      if (task.completed === true) {
        dictTasks[task.userId] += 1;
      }
    });
    console.log(dictTasks);
  }
});
