#!/usr/bin/node

$(document).ready(function () {
  $('div#add_item').click(function () {
    const newListItem = $('<li></li>').text('Item');
    $('ul.my_list').append(newListItem);
  });
});
