/*
do deep clone so that we can modified properties of objects
*/

function cloneObject(obj) {
  var clone = {};
  for (var i in obj) {
    if (typeof obj[i] == "object" && obj[i] != null)
      clone[i] = cloneObject(obj[i]);
    else clone[i] = obj[i];
  }
  return clone;
}

const obj = {
  a: "raj",
  b: 1231,
  c: {
    d: "asda",
    e: [12, 312, 31, 23],
    f: [{ name: "asda" }, { name: "nsasndan" }],
  },
};

const obj2 = cloneObject(obj);

obj.c.f[0].name = "bbbbb";
console.log(obj.c.f[0].name != obj2.c.f[0].name);
