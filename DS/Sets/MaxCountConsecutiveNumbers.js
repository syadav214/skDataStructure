const arr = [1, 3, 10, 2, 11, 4, 12];
const arrSet = new Set(arr);
let max = 0;
for (let ele of arrSet) {
  let count = 1;
  while (true) {
    ele++;
    if (arrSet.has(ele)) {
      count++;
    } else {
      break;
    }
  }
  if (count > max) {
    max = count;
  }
}

console.log(max);
