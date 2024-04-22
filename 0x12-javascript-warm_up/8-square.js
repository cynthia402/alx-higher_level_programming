#!/usr/bin/node

const argv = process.argv.slice(2);
const intNum = Number(argv[0]);

if (!isNaN(intNum)) {
  for (let i = 0; i < intNum; i++) {
    console.log('X'.repeat(intNum));
  }
} else {
  console.log('Missing size');
}
