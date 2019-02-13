const fn = a => console.log(a);
for (let i = 0; i < 3; i++) {
  setTimeout(function() {
    fn(i);
  }, 0);
}
console.log('x')
for (let i = 0; i < 3; i++) {
  setTimeout(function() {
    fn(i);
  }, 0);
}
