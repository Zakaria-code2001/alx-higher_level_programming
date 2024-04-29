#!/usr/bin/node

const fetch = require('node-fetch');

async function getMovieCharacters(movieId) {
    try {
        const url = `https://swapi.dev/api/films/${movieId}/`;

        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            const characterUrls = data.characters;

            for (const characterUrl of characterUrls) {
                const characterResponse = await fetch(characterUrl);
                if (characterResponse.ok) {
                    const characterData = await characterResponse.json();
                    console.log(characterData.name);
                } else {
                    console.log("Failed to fetch character details.");
                }
            }
        } else {
            console.log("Failed to fetch movie details.");
        }
    } catch (error) {
        console.error("An error occurred:", error);
    }
}

const movieId = 3;
getMovieCharacters(movieId);