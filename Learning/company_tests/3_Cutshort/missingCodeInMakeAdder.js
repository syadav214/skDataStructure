/*Fill the missing code

  function makeAdder(x) {
   // Fill the line
  }

  var add5 = makeAdder(5);

assert(add5(10) == 15);
*/

const assert = require('assert');
 function makeAdder(x) {
  return function(y) {
    return x + y;
  };
}

var add5 = makeAdder(5);

assert(add5(10) == 15);
