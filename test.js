function a(x) {
  return new Promise(resolve => {
    setTimeout(() => resolve(x), 2000);
  });
}

async function foo() {
  const a1 = await a(1);
  const a2 = await a(2);
  return a1+a2;
}

async function bar() {
  const a1 = a(3);
  const a2 = a(4);
  return await a1+ await a2;
}


foo().then(console.log)
bar().then(console.log)
console.log(await foo());
console.log(await bar());
