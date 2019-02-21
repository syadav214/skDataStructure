- Q1. What must be done in Javascript to implement Lexical scoping?

  A => Reference the current scope chain

- Q2. When browsers don't support a new feature developers turn to polyfills. How do these work>

  A => A polyfill implements an API so that developers can build against a consistent interface even on unsupported browers.

- Q3. How time it will take to execute below code?

```bash
  setTimeout(()=>console.log('hi'),1000);
  setTimeout(()=>console.log('hi'),1000);
  setTimeout(()=>console.log('hi'),1000);
  setTimeout(()=>console.log('hi'),1000);
  setTimeout(()=>console.log('hi'),1000);
```

A => 1 second.(All execute at once.)

- Q4. what does the expression {...store, dispatch} do?

```bash
  let store = {a:1,b:2};
  let dispatch = 3;
  console.log({...store,dispatch})
```

A => It creates new object with all keys and values from store and the key 'dispatch' mapped to the object.

- Q5. What is reason apps and frameworks are being built on top of immutable data structure?

  A => Immutable data structures make it easy to detect when variable values or nested values has changed.

- Q6. What is wrong in below code?

```bash
  class App extends Component {
    updateMessage(e){
      this.setState({msg:e.target.value});
    }

    render() {
      return (
        <input type='text' onChange={this.updateMessage}  value={this.state && this.state.msg}/>
      );
    }
  }
```

  A => updateMessage is not bound properly, so that this.setState will be undefined.
