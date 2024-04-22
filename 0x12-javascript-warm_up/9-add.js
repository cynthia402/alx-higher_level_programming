#!/usr/bin/node

const argv = process.argv.slice(2);
const c = Number(argv[0]);
const d = Number(argv[1]);

function add (a, b) {
  console.log(a + b);
}

add(c, d);
