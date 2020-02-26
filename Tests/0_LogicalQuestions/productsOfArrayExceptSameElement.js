console.log('------------Method 1---------------');
const input = [1, 2, 3, 4];
//output [ 24, 12, 8, 6 ]
const sum = input.reduce(
  (accumulator, currentValue) => accumulator * currentValue
);

let output = input.map(ele => {
  return sum / ele;
});

console.log('output1', output);
console.log('------------Method 2---------------');

output = [];
const leftProducts = [];
let prod = 1;
for (let i = 0; i < input.length; i++) {
  if (i == 0) {
    prod = 1;
  } else {
    prod *= input[i - 1];
  }

  leftProducts.push(prod);
}

const rightProducts = [];
prod = 1;
for (let i = input.length - 1; i > -1; i--) {
  if (i == input.length - 1) {
    prod = 1;
  } else {
    prod *= input[i + 1];
  }
  rightProducts.push(prod);
}

for (let i = 0; i < input.length; i++) {
  output.push(leftProducts[i] * rightProducts[input.length - 1 - i]);
}

console.log('output2', output);
