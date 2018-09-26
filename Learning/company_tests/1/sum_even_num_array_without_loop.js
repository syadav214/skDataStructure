let a = [1, 2, 3, 4, 5];

let b = a.filter(num => num % 2 === 0);

console.log(
  b.reduce((tot, num) => {
    return tot + num;
  })
);
