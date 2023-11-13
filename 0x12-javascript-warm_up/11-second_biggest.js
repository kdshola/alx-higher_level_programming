#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log(0);
} else if (process.argv[3] === undefined) {
  console.log(0);
} else {
  const args = process.argv.map(Number).slice(2).sort();
  const size = args.length;
  for (let index = size - 2; index >= 0; index--) {
    if (args[index] !== args[size - 1]) {
      console.log(args[index]);
      break;
    }
  }
}
