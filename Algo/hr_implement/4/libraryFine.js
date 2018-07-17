function libraryFine(d1, m1, y1, d2, m2, y2) {
  let fine = 0;
  if (y1 > y2) {
    fine = 10000;
  } else if (y1 <= y2) {
    if (m1 > m2 && y1 >= y2) {
      fine = 500 * (m1 - m2);
    } else if (m1 <= m2) {
      if (d1 > d2 && m1 - m2 >= 0 && y1 >= y2) {
        fine = 15 * (d1 - d2);
      } else {
        fine = 0;
      }
    }
  }
  return fine;
}

let d1 = 9,
  m1 = 6,
  y1 = 2015,
  d2 = 6,
  m2 = 6,
  y2 = 2015;
console.log(libraryFine(d1, m1, y1, d2, m2, y2));
