* Q1. What must be done in Javascript to implement Lexical scoping
  A => Reference the current scope chain

* Q2 . Fill the missing code
```bash
  const assert = require('assert');

  function makeAdder(x) {
   // Fill the line
  }

  var add5 = makeAdder(5);

assert(add5(10) == 15);
```
 A. 
 ```bash 
 const assert = require('assert');
 function makeAdder(x) {
  return function(y) {
    return x + y;
  };
}

var add5 = makeAdder(5);

assert(add5(10) == 15);
```



