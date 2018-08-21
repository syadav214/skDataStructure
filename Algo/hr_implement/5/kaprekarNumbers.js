function kaprekarNumbers(p, q) {
  for (let i = p; i <= q; i++) {
    let sqr_i = i * i;
    let remainder_sqr = sqr_i % Math.pow(10, i.toString().length);
    let divisor_sqr = Math.floor(sqr_i / Math.pow(10, i.toString().length));

    if (remainder_sqr + divisor_sqr == i) {
      console.log('Got it ', i);
    }
  }
}

kaprekarNumbers(1, 100);
