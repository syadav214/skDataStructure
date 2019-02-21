let x = 2;
let y = 4;

if ((y > x || y++ === 4) && ++y === 5) {
  console.log(1);
} else {
  console.log(2);
}

console.log(y);
