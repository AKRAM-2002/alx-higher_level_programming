#!/usr/bin/node
const args = process.argv.slice(2);
function factorial(n) {
    if (isNaN(n)) {
        return 1;
    }
    n = parseInt(n, 10);

    if (n === 0 || n === 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
const input = args[0];
const result = factorial(input);
if (!isNaN(result) && isFinite(result)) {
    console.log(result);
} else {
    console.log("Infinity");
}