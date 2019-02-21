function getPower(num, exp) {
  let power = 1,
    negative = false;

  if (exp < 0) {
    negative = true;
    exp = Math.abs(exp);
  }

  for (let i = 1; i <= exp; i++) {
    power = power * num;
  }

  if (negative) {
    power = 1 / power;
  }

  return power;
}

console.log(getPower(2, -5));
