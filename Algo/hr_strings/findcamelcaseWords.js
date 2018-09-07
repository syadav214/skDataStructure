function camelcase(s) {
  let count = 1;
  for (let w in s) {
    let asciiVal = s[w].charCodeAt(0);
    if (asciiVal >= 65 && asciiVal <= 90) {
      count++;
    }
  }
  return count;
}
console.log('Ans: ', camelcase('saveChangesInTheEditor'));
