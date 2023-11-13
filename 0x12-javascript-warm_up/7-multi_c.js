#!/usr/bin/node
const myString = 'C is fun';
const count = Math.floor(Number(process.argv[2]));
if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let value = 0; value < count; ++value) {
    console.log(myString);
  }
}
