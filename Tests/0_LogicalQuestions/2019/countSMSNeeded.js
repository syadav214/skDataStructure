const s = 'SMS messages are really short';
const k = 12;

let currLen = s.length,
  start = 0,
  cnt = 0;
const a = s.split(' ');

while (currLen > start) {
  let word = s.substring(start, start + k);
  word = word.trim();

  const wordArr = word.split(' ');
  wordArr.map(w => {
    if (a.includes(w) === false) {
      cnt = -1;
    }
  });

  if (cnt === -1) {
    break;
  }

  start += k;
  cnt++;
}

console.log('count', cnt);
