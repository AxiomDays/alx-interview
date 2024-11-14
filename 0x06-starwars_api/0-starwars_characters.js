#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2]

function firstGet(){
	i == 0
	request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, async function(error, response, body) {
	function recurse(i){
		const res = JSON.parse(body) // Print the HTML for the Google homepage.
		truth(res, i)
		recurse(i++)

	}
	
});
}

function truth(res, j){
	request(res["characters"][j], async function(error, response, innerBody){
	console.log(JSON.parse(innerBody)["name"]);
});
}

/*function theLoop(res){
for (let i = 0; i < res["characters"].length; i++){
	console.log("")
	truth(res, i);
}
}*/

firstGet();
