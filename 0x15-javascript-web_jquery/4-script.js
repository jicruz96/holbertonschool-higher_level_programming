$('DIV#toggle_header').click(function () {
  const headers = $('header');

  if (headers.hasClass('red')) {
    headers.removeClass('red');
    headers.addClass('green');
  } else {
    headers.removeClass('green');
    headers.addClass('red');
  }
});
