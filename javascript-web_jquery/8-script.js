#!/usr/bin/node

$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $.each(data.results, function (i, movie) {
      $('<li>').text(movie.title).appendTo('#list_movies');
    });
  });
});
