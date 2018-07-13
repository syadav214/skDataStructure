function appendAndDelete(s, t, k) {
    if (s.length + t.length < k) {
      return 'Yes';
    }
    let diff = 0;
    for (let i in s) {
      if (i >= t.length) {
        diff = i;
        break;
      } else if (s[i] != t[i]) {
        diff = i;
        break;
      }
    }
    diff = s.length - diff + (t.length - diff);
  
    if (diff <= k && (diff - k) % 2 == 0) {
      return 'Yes';
    } else {
      return 'No';
    }
  }
  
  let s = 'hackerhappy',
    t = 'hackerrank',
    k = 9;
  console.log(appendAndDelete(s, t, k));
  