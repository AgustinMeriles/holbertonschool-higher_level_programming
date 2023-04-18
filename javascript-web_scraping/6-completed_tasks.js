#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get({ apiUrl }, (error, response, data) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = data;
    const completedTskByUser = {};

    tasks.forEach(task => {
      if (task.completed) {
        const userId = task.id;
        completedTskByUser[userId]++;
      }
    });
    console.log(completedTskByUser);
  }
});
