let fn = function() {
    return {
      val: '1',
      log: function() {
        console.log(this.val);
      }
    };
  };
  
  fn().log();
  
  let fn2 = function() {
    return {
      val: '1',
      log: () => {
          // will print undefined
        console.log(this.val);
      }
    };
  };
  
  fn2().log();
  