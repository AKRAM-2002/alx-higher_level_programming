#!/usr/bin/node
// a script that prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const URL = process.argv[2];
let count = 0;


request.get(URL, function(err, response){
    if(err){
        console.log(err);
        return;
    }
    else {
        const data = JSON.parse(response.body);
        for (let i = 0; i < data.results.length; i++) {
            for (let j = 0; j < data.results[i].characters.length; j++) {
                if (data.results[i].characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
                    count++;
                }
            }
        }
        console.log(count);
    }
    
})