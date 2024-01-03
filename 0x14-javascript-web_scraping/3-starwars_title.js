#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const respJSON = JSON.parse(body);
    console.log(respJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
