function reduce(s) {
  let obj = {};
  for (let i = 0; i < s.length; i++) {
    if (s[i] == s[i + 1]) {
      s = s.replace(s[i] + s[i + 1], '');
      obj = { all: false, val: s };
      return obj;
      break;
    }
  }
  obj = { all: true, val: s };
  return obj;
}

function superReducedString(s) {
  let allDone = false;
  while (allDone == false) {
    let obj = reduce(s);
    allDone = obj.all;
    s = obj.val;
  }

  if (s == '') {
    return 'Empty String';
  }

  return s;
}

console.log(superReducedString('aaabccddd'));
