#!/usr/bin/node

const argv = process.argv.slice(2);
const intnum = Number(argv[0]);

if (!isNaN(intnum)) {
  console.log('My number: ' + Math.floor(intnum));
} else {
  console.log('Not a number');
}
