$('DIV#red_header').click(function () {
  const headers = $('header');

  if (headers.hasClass('red')) {
    headers.removeClass('red');
  } else {
    headers.addClass('red');
  }
});
