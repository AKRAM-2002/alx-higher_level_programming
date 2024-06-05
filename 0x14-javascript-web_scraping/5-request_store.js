#!/usr/bin/node
// Script that gets the content of a webpage and stores it in file

const fs  = require('fs');
const request = require('request');

const URL = process.argv[2];
const filename = process.argv[3];


request.get(URL, function (err, res) {
    if (err) {
        console.log(err);
        return;
    }
    fs.writeFile(filename, res.body, (err) => {
        if (err) {
            console.log(err);
            return;
        }
    });
})