// [15, 2, 4, 8, 9, 5, 10, 23]
// 33
// 14

// Given an unsorted array of nonnegative integers,
// find a continuous subarray that adds to a given number.

const isSumArrayPresent = (arr, sum) => {
  for (let i = 0; i < arr.length; i++) {
    let currSum = arr[i];
    for (let j = i + 1; j < arr.length; j++) {
      currSum += arr[j];
      if (currSum === sum) {
        return true;
      } else if (currSum > sum) {
        break;
      }
    }
  }
  return false;
};

console.log(isSumArrayPresent([15, 2, 4, 8, 9, 5, 10, 23], 33));
console.log(isSumArrayPresent([15, 2, 4, 8, 9, 5, 10, 23], 14));
console.log(isSumArrayPresent([15, 2, 4, 8, 9, 5, 10, 23], 18));
