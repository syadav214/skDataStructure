function nonDivisibleSubset(a, k) {
  let total = 0,
    counts = [];

  for (let i = 0; i < k + 1; i++) {
    counts[i] = 0;
  }

  for (let i = 0; i < a.length; i++) {
    counts[a[i] % k] += 1;
  }

  total = Math.min(counts[0], 1);

  let upto = Math.floor(k / 2);
  if (upto * 2 == k) {
    upto -= 1;
  }

  for (let i = 1; i <= upto; i++) {
    total += Math.max(counts[i], counts[k - i]);
  }

  return total;
}

let a = [1, 7, 4, 2],
  k = 3;
console.log(nonDivisibleSubset(a, k));
