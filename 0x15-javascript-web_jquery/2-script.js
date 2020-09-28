$('#red_header').click(function () {
  const color = $(this).css('color');

  if (color === 'rgb(255, 0, 0)') {
    $(this).css('color', 'black');
  } else {
    $(this).css('color', 'red');
  }
});
