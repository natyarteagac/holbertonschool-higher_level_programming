$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
  $.each(data.results, function (index, variable) {
    $('UL#list_movies').append('<li>' + variable.title + '</li>');
  });
});
