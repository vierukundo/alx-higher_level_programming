$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(data) {
      let $moviesList = $('UL#list_movies');

      $.each(data.results, function(i, film) {
        $moviesList.append('<li>' + film.title + '</li>');
      });
    }
});
