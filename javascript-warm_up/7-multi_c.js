#!/usr/bin/node

if (process.argv[2]) {
  const text = 'C is fun';
  const x = process.argv[2];
  for (let i = 0; i < x; i++) {
    console.log(text);
  }
} else {
  console.log('Missing number of occurrences');
}
