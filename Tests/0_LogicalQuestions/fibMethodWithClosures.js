function fibMethod() {
    let arr = [0, 1];
  
    function getFib() {
      let len = arr.length;
      let num = arr[len - 1];
      arr.push(arr[len - 1] + arr[len - 2]);
      return num;
    }
    return getFib;
  }
  
  var getFib = fibMethod();
  console.log(getFib());
  console.log(getFib());
  console.log(getFib());
  console.log(getFib());
  console.log(getFib());
  