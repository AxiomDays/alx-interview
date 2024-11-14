#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

function firstGet () {
  request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, function (error, response, body) {
    const res = JSON.parse(body).characters;
    const newArr = res.map(
      url => new Promise((resolve, reject) => {
        request(url, function (error, response, innerBody) {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(innerBody).name);
        });
      }));

    Promise.all(newArr)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
if (process.argv.length > 2) {
  firstGet();
}
