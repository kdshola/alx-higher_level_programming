$(() => {
  function say_hello () {
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
  }
  $('#btn_translate').click(() => {
    say_hello();
  });

  $('#language_code').keypress((evnt) => {
    if (evnt.which === 13) {
      say_hello();
    }
  });
});
