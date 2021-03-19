// "<div><div><b></b></div></p>"
function StringChallenge(str) {
  const arr = str.split(">");

  const firstElement = arr[0];
  const lastElement = arr[arr.length - 1].replace("/", "");

  // code goes here
  return firstElement == lastElement ? true : firstElement + ">";
}

// keep this function call here
console.log(StringChallenge(readline()));
