#!/usr/bin/node

$(document).ready(function() {
    $("div#toggle_header").click(function() {
      var currentClass = $("header").attr("class");
      if (currentClass == "green") {
        $("header").removeClass("green").addClass("red");
      } else {
        $("header").removeClass("red").addClass("green");
      }
    });
  });