/*
1. the settimeout should print unique value => use let instead of var
2. multiple in timeout, so that it will wait else all get printed once
*/

for (let i = 0; i < 10; i++) {
  setTimeout(() => {
    console.log(i);
  }, 1000 * i);
}
