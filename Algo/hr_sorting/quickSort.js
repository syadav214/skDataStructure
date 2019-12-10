const arr = [5, 8, 3, 2, 4];
quickSort(arr, 0, arr.length - 1);
console.log('final', arr);

function getPivot(arr, start, end) {
  let pi = arr[end];
  let smallIndex = start - 1;
  for (let i = start; i < end; i++) {
    if (arr[i] <= pi) {
      smallIndex++;
      let temp = arr[smallIndex];
      arr[smallIndex] = arr[i];
      arr[i] = temp;
    }
  }

  smallIndex++;
  let temp = arr[smallIndex];
  arr[smallIndex] = arr[end];
  arr[end] = temp;

  return smallIndex;
}

function quickSort(arr, start, end) {
  if (start < end) {
    let piIndex = getPivot(arr, start, end);
    quickSort(arr, start, piIndex - 1);
    quickSort(arr, piIndex + 1, end);
  }
}
