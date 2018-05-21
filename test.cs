
class ItemOrder {
    ItemOrder(Product obj) {
        this.Product = obj;
    }
}

//base
class Product {
    Product() {}
}

//child 1
class Item: Product {
    Item(id) {
        this.id = id;
        this.name = 'Item';
    }
}

//child 2
class Discount: Product {
    Discount(id) {
        this.id = id;
        this.name = 'Discount';
    }
}

var i = new Item(1);
Console.WriteLine(i);