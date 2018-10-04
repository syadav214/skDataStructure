var gcd = function(a, b) {
  console.log('b', !b, a, b);
  if (!b) {
    return a;
  }

  return gcd(b, a % b);
};

console.log(gcd(5, 15));
