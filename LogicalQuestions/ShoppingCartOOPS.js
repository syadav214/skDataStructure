class ItemOrder {
    constructor(obj, qty) {
        this.Product = obj;
        this.qty = qty;
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
    }

    getName(id) {
        return this.name;
    }

    getPrice(id) {
        return this.price;
    }
}

//child 2
class Discount extends Product {
    constructor(id, name) {
        super();
        this.id = id;
        this.name = name;
    }

    getName(id) {
        return this.name;
    }

    getDiscount(id) {
        return this.discount;
    }
}

var ListOfOrder = [];
var i = new Item(1);
var d = new Discount(10);

var io = new ItemOrder(i, 1);
ListOfOrder.push(io);

io = new ItemOrder(d, 1);
ListOfOrder.push(io);

console.log(ListOfOrder);
console.log(ListOfOrder[0].Product);
console.log(ListOfOrder[1].Product)