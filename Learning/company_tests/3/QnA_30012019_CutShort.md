* Q1. What must be done in Javascript to implement Lexical scoping?

  A => Reference the current scope chain

* Q2. When browsers don't support a new feature developers turn to polyfills. How do these work>

  A => A polyfill implements an API so that developers can build against a consistent interface even on unsupported browers.

* Q3. Why does below quirks happen?

```bash
  console.log(.1+.2); //0.30000000000000004
```

  A => This is an inherent limitation of floating point that JS shares with other languages.

* Q4. what does the expression {...store, dispatch} do?

```bash
  let store = {a:1,b:2};
  let dispatch = {};
  console.log({...store,dispatch})
```

  A => It creates new object with all keys from store and dispatch.




