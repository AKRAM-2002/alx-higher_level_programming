#!/usr/bin/node
//a script that display the status code of a GET request.
const request = require('request');
const url =  process.argv[2];
request.get(url, function (error, response, body) {
    if (error) {
        console.log(error);
        return;
    }
    console.log('code:', response && response.statusCode); 
        
});