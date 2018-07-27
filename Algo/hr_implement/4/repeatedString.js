function repeatedString(s, n) {
  let loops = Math.floor(n / s.length);

  let remainder = n % s.length;
  let cnt = 0,
    extra_a = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] == 'a') {
      cnt++;
      if (i < remainder) {
        extra_a++;
      }
    }
  }

  cnt = cnt * loops + extra_a;
  return cnt;
}

let s = 'aba',
  n = 10;
console.log(repeatedString(s, n));
