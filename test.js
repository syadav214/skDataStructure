const arr = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

const r = 3,
  c = 3;

let swapDone = {};

for (let i = 0; i < r; i++) {
  for (let j = 0; j < c; j++) {
    if (i !== j) {
      if (swapDone[i + ':' + j] !== true) {
        let temp = arr[i][j];
        arr[i][j] = arr[j][i];
        arr[j][i] = temp;
        swapDone[j + ':' + i] = true;
      }
    }
  }
}

for (let i = 0; i < r; i++) {
  for (let j = 0; j < 1; j++) {
    let temp = arr[i][j];
    arr[i][j] = arr[i][r - 1];
    arr[i][r - 1] = temp;
  }
}

console.log(arr);
