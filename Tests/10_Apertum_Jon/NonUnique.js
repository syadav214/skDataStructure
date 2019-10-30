function countNonUnique(numbers) {
  let numMap = new Map();
  numbers.map(ele => {
    if (numMap[ele]) {
      numMap[ele] = numMap[ele] + 1;
    } else {
      numMap[ele] = 1;
    }
  });
  let count = 0;
  for (let c in numMap) {
    if (numMap[c] >= 2) {
      count++;
    }
  }
  console.log(numMap);
  return count;
}
