$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: (response) => {
      $('#hello').text(response.hello);
    }
  });
});
