#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url =  ''
fs.unlink('txt',(err) => {
    if (err) {
      console.error('Error deleting file:', err);
      return;
    }
    console.log('File deleted successfully');
  });
    request('https://github.com/mdn/learning-area/blob/main/javascript/oojs/tasks/json/sample.json', function (error, response, body) {
        console.error('error:', error); // Print the error if one occurred
        console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
        
});