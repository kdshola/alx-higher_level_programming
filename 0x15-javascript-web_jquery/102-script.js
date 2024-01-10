$(() => {
  $('#btn_translate').click(() => {
    const input = $('#language_code').val();
    const api = 'https://www.fourtonfish.com/hellosalut/hello/';
    $.ajax({
      type: 'GET',
      url: api,
      data: { lang: input },
      success: (response) => {
        $('#hello').text(response.hello);
      }
    });
  });
});
