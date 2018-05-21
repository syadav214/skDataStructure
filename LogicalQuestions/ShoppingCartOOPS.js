class ItemOrder {
    constructor(obj) {
        this.Product = obj;
    }
}

//base
class Product {
    constructor() {}
}

//child 1
class Item extends Product {
    constructor(id) {
        super();
        this.id = id;
        this.name = 'Item';
    }
}

//child 2
class Discount extends Product {
    constructor(id) {
        super();
        this.id = id;
        this.name = 'Discount';
    }
}

var ListOfOrder = [];
var i = new Item(1);
//console.log(i.name)

var im = new ItemOrder(i);
//console.log(im);
ListOfOrder.push(im);

var d = new Discount(1);
//console.log(d.name);

im = new ItemOrder(d);
//console.log(im);
ListOfOrder.push(im);

console.log(ListOfOrder);
console.log(ListOfOrder[0].Product);
console.log(ListOfOrder[1].Product)