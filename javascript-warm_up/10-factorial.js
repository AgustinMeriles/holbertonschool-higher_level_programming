#!/usr/bin/node

const number = parseInt(process.argv[2]);

function fact (n) {
  const arr = [];
  while (n !== 0) {
    arr.push(n);
    n--;
  }
  let result = arr[0];
  for (let i = 1; i < arr.length; i++) {
    result *= arr[i];
  }
  return result;
}

if (isNaN(number)) {
  console.log(1);
} else {
  console.log(fact(number));
}
