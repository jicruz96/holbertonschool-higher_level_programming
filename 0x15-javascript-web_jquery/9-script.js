const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$().ready(function () {
  $.getJSON(url, function (data) {
    $('div#hello').text(data.hello);
  });
});
