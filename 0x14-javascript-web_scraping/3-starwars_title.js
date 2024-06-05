#!/usr/bin/node
// a script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const integer = process.argv[2]
const endpoint = `https://swapi-api.alx-tools.com/api/films/${integer}`

request.get(endpoint, function(err, response){
    if(err){
        console.log(err);
        return;
    }
    console.log(JSON.parse(response.body).title);
})