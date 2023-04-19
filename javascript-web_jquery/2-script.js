#!/usr/bin/node

document.querySelector('DIV#red_header').addEventListener('click', changeColor);

function changeColor () {
  $('header').css('color', '#FF0000');
}
