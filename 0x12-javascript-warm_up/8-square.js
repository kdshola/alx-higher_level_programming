#!/usr/bin/node
const count = Math.floor(Number(process.argv[2]));
if (isNaN(count)) {
  console.log('Missing size');
} else {
  for (let value = 0; value < count; ++value) {
    console.log('X'.repeat(count));
  }
}
