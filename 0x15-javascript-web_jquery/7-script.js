/*
a JavaScript script that fetches the character name from this
URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

The name must be displayed in the HTML tag DIV#character
*/

$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  const charcter = data.name;
  $('div#character').text(charcter);
})
  .fail(function (jqXHR, Status, errorThrown) {
    console.error('Error:' + errorThrown);
  });
