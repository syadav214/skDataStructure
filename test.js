let object1 = {
  name:'abc',
  items:[
      {item_name:'123'},
      {item_name:'456'}
  ]
}

for(let x in object1) {
  console.log(object1[x],Array.isArray(object1[x]))
}

