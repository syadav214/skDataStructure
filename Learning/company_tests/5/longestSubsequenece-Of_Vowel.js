longestSubsequence('aeiaaioooaauuaeiou');

function longestSubsequence(s) {
  const vowel = ['a', 'e', 'i', 'o', 'u'];
  let pos = 0;
  let cnt = 0;
  let prevCh = '';
  s.split('').map(ch => {
    if (prevCh === ch) {
      cnt++;
    } else if (ch === vowel[pos]) {
      cnt++;
      pos++;
    }
    prevCh = ch;
  });
  console.log('pos',pos)
  if (pos  < 5) {
    cnt = 0;
  }
  console.log(cnt);
}
