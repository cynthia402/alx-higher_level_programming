/*
a JavaScript script that toggles the class of the <header> element
when the user clicks on the tag DIV#toggle_header
*/

$('DIV#red_header').click(function () {
  if ($(this).hasClass('red')) {
    $(this).removeClass('red').addClass('green');
  } else {
    $(this).removeClass('green').addClass('red');
  }
});
