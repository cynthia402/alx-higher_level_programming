#!/usr/bin/node

const argv = process.argv.slice(2);
const intNum = Number(argv[0]);
let i = 0;

if (!isNaN(intNum)) {
  while (i++ < intNum) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
