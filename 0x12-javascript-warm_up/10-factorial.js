#!/usr/bin/node

const arg = process.argv.slice(2)[0];
function factorial (args) {
  if (args === 1 || isNaN(args)) {
    return 1;
  }
  return (args * factorial(args - 1));
}

console.log(factorial(Number(arg)));
