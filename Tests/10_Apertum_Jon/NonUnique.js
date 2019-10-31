const numbers = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2];

const numMap = {};// OR const numMap = new Map();
numbers.map(ele => {
  if (numMap[ele]) {
    numMap[ele]++;
  } else {
    numMap[ele] = 1;
  }
});
let count = 0;
for (const c in numMap) {
  if (numMap[c] >= 2) {
    count++;
  }
}
console.log({ numMap, count });
