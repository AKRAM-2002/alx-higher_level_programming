#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
const request = require('request');
const URL = process.argv[2];

request.get(URL, function(err, response, body){
    if(err){
        console.log(err);
        return;
    }
    const data = JSON.parse(response.body);
    let tasksCompleted = {};
    for (let i = 0; i < data.length; i++) {
        if (tasksCompleted[data[i].userId] === undefined) {
            tasksCompleted[data[i].userId] = 0;
        }
        if (data[i].completed === true) {
            tasksCompleted[data[i].userId]++;
        }
    }
    // const users = Object.keys(tasksCompleted).sort();
    // console.log(users);
    console.log(tasksCompleted)
});