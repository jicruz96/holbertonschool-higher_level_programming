const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (data) {
  const results = data.results;
  let i;

  for (i = 0; i < data.count; i++) {
    $('UL#list_movies').append(`<li>${results[i].title}</li>`);
  }
});
