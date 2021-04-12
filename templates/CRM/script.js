$('.js-data-example-ajax').select2({
    ajax: {
      url: 'https://api.github.com/search/repositories',
      dataType: 'json'
      // Additional AJAX parameters go here; see the end of this chapter for the full code of this example
    }
  });