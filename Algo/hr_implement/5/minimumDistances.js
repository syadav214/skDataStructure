function minimumDistances(a) {
  let minArray = [];
  for (let i = 0; i < a.length; i++) {
    for (let j = i + 1; j < a.length; j++) {
      if (a[i] == a[j]) {
        let diff = i - j;
        if (diff < 0) {
          diff = -1 * diff;
        }
        minArray.push(diff);
      }
    }
  }

  if (minArray.length == 0) {
    return -1;
  } else {
    return Math.min(...minArray);
  }
}

let a = [7, 1, 3, 4, 1, 7];
console.log(minimumDistances(a));
