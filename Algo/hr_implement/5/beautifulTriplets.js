function beautifulTriplets(d, a) {
  let count = 0;
  for (let i = a.length - 1; i > 0; i--) {
    for (let j = i - 1; j > -1; j--) {
      if (a[i] - a[j] == d) {
        for (let k = j - 1; k > -1; k--) {
          if (a[j] - a[k] == d) {
            count++;
          }
        }
      }
    }
  }
  return count;
}

let a = [1, 2, 4, 5, 7, 8, 10];
console.log(beautifulTriplets(3, a));
