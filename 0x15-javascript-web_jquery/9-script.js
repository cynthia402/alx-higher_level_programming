/*
a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
and displays the value of hello from that fetch in the HTML tag DIV#hello.
*/

$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  const hello = data.hello;
  $('DIV#hello').text(hello);
})
  .fail(function (jqXHR, status, error) {
    console.error(error);
  });
