#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

if (process.argv[2]) {
  request(url, async (error, response, data) => {
    if (error) {
      console.log(error);
      return;
    }
    if (response) {
      const res = JSON.parse(data);
      const characters = res.characters;
      const tasks = characters.map(character => {
        return new Promise((resolve, reject) => {
          request(character, (err, res, data) => {
            if (err) {
              reject(err);
            }
            if (data) {
              const character = JSON.parse(data);
              resolve(character.name);
            }
          });
        });
      });
      await Promise.allSettled(tasks).then((results) => {
        results.forEach(res => (console.log(res.value)));
      }).catch((error) => {
        console.log(error);
      });
    }
  });
}
