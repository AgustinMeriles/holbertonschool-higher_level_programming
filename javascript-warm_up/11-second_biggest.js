#!/usr/bin/node

if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const newArr = process.argv.slice(2).map(Number);
  const mayor = Math.max(...newArr);
  const sinMayor = newArr.filter(n => n !== mayor);
  if (sinMayor.length > 0) {
    const segMayor = Math.max(...sinMayor);
    console.log(segMayor);
  } else {
    console.log(0);
  }
}
