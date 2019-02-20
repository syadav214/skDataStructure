p = [-2, 3, 1, -5];

let start = 1;
startedWith = start;
for (let i = p.length - 1; i >= 0; i--) {
  if (p[i] < 0) {
    start += -1 * p[i];
  } else {
    start -= p[i];
  }
}
