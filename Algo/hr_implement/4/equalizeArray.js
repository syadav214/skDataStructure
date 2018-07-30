function equalizeArray(a) {
  let max = 0,
    hashMap = new Map();
  for (let i = 0; i < a.length; i++) {
    let val = 1;
    if (hashMap.has(a[i])) {
      val = hashMap.get(a[i]) + 1;
      hashMap.delete(a[i]);
    }
    hashMap.set(a[i], val);
    if (val > max) {
      max = val;
    }
  }
  return a.length - max;
}

let a = [3, 3, 1, 2, 3];
console.log('ans: ', equalizeArray(a));
