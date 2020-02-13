$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  data.results.forEach(function (movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
