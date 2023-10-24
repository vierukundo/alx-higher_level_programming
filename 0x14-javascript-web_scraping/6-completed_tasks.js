#!/usr/bin/node
// Script that computes the number of tasks completed by user id

if (process.argv.length !== 3) {
  console.error('Invalid number of arguments!');
  process.exit(1);
}

const url = process.argv[2];

const request = require('request');

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const userCompletedTasks = {};

    // Loop through the tasks and count completed tasks for each user
    for (const task of body) {
      if (task.completed) {
        const userId = task.userId;

        if (userCompletedTasks[userId]) {
          userCompletedTasks[userId] += 1;
        } else {
          userCompletedTasks[userId] = 1;
        }
      }
    }

    // Print users with completed tasks
    console.log(userCompletedTasks);
  } else {
    console.error('Request failed. Status code:', response.statusCode);
  }
});
