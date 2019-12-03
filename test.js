const arr = [5, 8, 3, 2, 4];
quickSort(arr, 0, arr.length - 1);
console.log('arr', arr);

function partition(arr, low, high) {
  let pi = arr[high];
  let index = low - 1;

  for (let j = low; j <= high - 1; j++) {
    if (arr[j] <= pi) {
      index++;
      let temp = arr[index];
      arr[index] = arr[j];
      arr[j] = temp;
    }
  }
  let temp = arr[index + 1];
  arr[index + 1] = arr[high];
  arr[high] = temp;

  return index + 1;
}

function quickSort(arr, low, high) {
  if (low < high) {
    let pi = partition(arr, low, high);
    quickSort(arr, low, pi - 1);
    quickSort(arr, pi + 1, high);
  }
}
