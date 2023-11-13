#!/usr/bin/node

function factorial (number) {
  if (isNaN(number) || (number === 0)) {
    return 1;
  }
  return number * factorial(number - 1);
}

const input = Math.floor(Number(process.argv[2]));
console.log(factorial(input));
