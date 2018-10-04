let a = [5, -1, 3, 8, 6];
a.sort();

let mid = 0;
if (a.length % 2 == 0) {
  mid = a.length / 2;
} else {
  mid = (a.length + 1) / 2;
}

/*
using splice
let min = a.splice(0, mid);
let max = a;
*/
let min = a.slice(0, mid);
let max = a.slice(mid);

console.log(min, max);
