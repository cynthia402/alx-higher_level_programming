/*
 a JavaScript script that fetches and lists the title for all movies by using this
URL: https://swapi-api.alx-tools.com/api/films/?format=json
 All movie titles must be list in the HTML tag UL#list_movies
*/

$.get.JSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const results = data.results;
  for (const move of results) {
    $('UL#list_movies').append('<li>' + move.title + '</li>');
  }
})

  .fail(function (jqXHR, status, error) {
    console.error(error);
  });
