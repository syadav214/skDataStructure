// [15, 2, 4, 8, 9, 5, 10, 23]
// 33
// 14

// Given an unsorted array of nonnegative integers,
// find a continuous subarray that adds to a given number.

const isSumArrayPresent = (arr, sum) => {
  let currSum = arr[0],
    start = 0,
    n = arr.length;
  for (let i = 1; i <= n; i++) {
    while (currSum > sum && start < i - 1) {
      currSum -= arr[start];
      start++;
    }

    if (currSum === sum) {
      return true;
    }

    if (i < n) {
      currSum += arr[i];
    }
  }
  return false;
};

console.log(isSumArrayPresent([15, 2, 4, 8, 9, 5, 10, 23], 33));
console.log(isSumArrayPresent([15, 2, 4, 8, 9, 5, 10, 23], 14));
console.log(isSumArrayPresent([15, 2, 4, 8, 9, 5, 10, 23], 18));
