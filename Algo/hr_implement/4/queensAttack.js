/*
You will be given a square chess board with one queen and a number of obstacles placed on it.
Determine how many squares the queen can attack. We do not have count positions which are obstructed.
*/
function queensAttack(n, k, r_q, c_q, obstacles) {
  if (n === 1) {
    return 0;
  }

  let moves = 0,
    obsMap = new Map();

  for (let i = 0; i < k; i++) {
    obsMap.set(
      obstacles[i][0].toString() + '-' + obstacles[i][1].toString(),
      1
    );
  }

  for (let x = 1; x <= 8; x++) {
    let r = r_q,
      c = c_q,
      finished = false;

    while (!finished) {
      switch (x) {
        case 1:
          r++;
          c--;
          break;
        case 2:
          r--;
          c++;
          break;
        case 3:
          r--;
          c--;
          break;
        case 4:
          r++;
          c++;
          break;
        case 5:
          r++;
          break;
        case 6:
          r--;
          break;
        case 7:
          c--;
          break;
        case 8:
          c++;
          break;
      }

      if (
        r > n ||
        c > n ||
        r < 1 ||
        c < 1 ||
        obsMap.has(r.toString() + '-' + c.toString())
      ) {
        finished = true;
        break;
      }

      moves++;
    }
  }
  return moves;
}

let n = 5,
  k = 3,
  r_q = 4,
  c_q = 3;
let obstacles = [];
obstacles.push([5, 5]);
obstacles.push([4, 2]);
obstacles.push([2, 3]);

console.log(queensAttack(n, k, r_q, c_q, obstacles));
