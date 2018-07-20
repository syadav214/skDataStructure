function cutTheSticks(arr) {
  let result = [];
  let len_arr = arr.length;
  result.push(len_arr);
  while (len_arr > 0) {
    let smallest_number = Math.min(...arr);
    let new_arr = [];
    for (let i = 0; i < len_arr; i++) {
      if (smallest_number != arr[i]) {
        new_arr.push(arr[i] - smallest_number);
      }
    }
    arr = new_arr;
    len_arr = arr.length;
    if (len_arr == 0) {
      break;
    }
    result.push(len_arr);
  }
  return result;
}

let arr = [1, 2, 3, 4, 3, 3, 2, 1];
console.log(cutTheSticks(arr));
