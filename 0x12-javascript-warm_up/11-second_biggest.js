#!/usr/bin/node

let args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  args = args.map(Number);
  args = args.sort(function (a, b) { return a - b; });
  console.log(args[args.length - 2]);
}
