//["OOOO", "OOFF", "OCHO", "OFOO"]
function SearchingChallenge(strArr) {
  const foodLocation = [];
  let dogLocation = [];
  let homeLocation = [];

  for (let i in strArr) {
    const single = strArr[i];
    for (let s in single) {
      if (single[s] === "C") {
        dogLocation.push(parseInt(i));
        dogLocation.push(parseInt(s));
      } else if (single[s] === "F") {
        foodLocation.push([parseInt(i), parseInt(s)]);
      } else if (single[s] === "H") {
        homeLocation.push(parseInt(i));
        homeLocation.push(parseInt(s));
      }
    }
  }

  let min = Number.MAX_VALUE,
    minIndex = -1,
    lastMinIndex = -1,
    steps = 0,
    totalLoop = 0;
  while (totalLoop < foodLocation.length) {
    let arrToCompare;
    if (lastMinIndex > -1) {
      arrToCompare = foodLocation[minIndex];
    } else {
      arrToCompare = dogLocation;
    }

    for (let i = 0; i < foodLocation.length; i++) {
      if (i == lastMinIndex) {
        continue;
      }

      const single = foodLocation[i];
      const dis = getDistance(
        single[0],
        single[1],
        arrToCompare[0],
        arrToCompare[1]
      );
      if (dis < min) {
        min = dis;
        minIndex = i;
      }
    }

    lastMinIndex = minIndex;
    totalLoop++;
    steps += min;

    min = Number.MAX_VALUE;
  }

  const lastLocation = foodLocation[lastMinIndex];
  const dis = getDistance(
    lastLocation[0],
    lastLocation[1],
    homeLocation[0],
    homeLocation[1]
  );
  steps += dis;

  return steps;
}

function getDistance(x1, y1, x2, y2) {
  let x = x1 - x2,
    y = y1 - y2;
  if (x < 0) {
    x = x * -1;
  }
  if (y < 0) {
    y = y * -1;
  }
  return x + y;
}

// keep this function call here
console.log(SearchingChallenge(readline()));
