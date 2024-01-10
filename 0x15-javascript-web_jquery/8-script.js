$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (response) => {
      $.each(response.results, (index, object) => {
        $('#list_movies').append('<li>' + object.title + '</li>');
      });
    }
  });
});
