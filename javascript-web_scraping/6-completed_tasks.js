#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get({ url: apiUrl }, (error, response, data) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(data);
    const completedTskByUser = {};

    tasks.forEach(task => {
      if (task.completed) {
        const userId = task.userId;
        completedTskByUser[userId] = (completedTskByUser[userId] || 0) + 1;
      }
    });
    console.log(completedTskByUser);
  }
});
