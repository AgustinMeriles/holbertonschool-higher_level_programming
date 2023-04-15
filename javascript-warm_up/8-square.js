#!/usr/bin/node

const number = parseInt(process.argv[2]);
const txt = 'x';
let i;
let p = '';

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (i = 0; i < number; i++) {
    p = '';
    for (let y = 0; y < number; y++) {
      p += txt;
    }
    console.log(p);
  }
}
