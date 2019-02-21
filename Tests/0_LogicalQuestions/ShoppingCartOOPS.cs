public class ItemOrder
    {
        Product _prodObj;
        public ItemOrder(Product obj)
        {
            this._prodObj = obj;
        }
    }

    //base
    public class Product
    {
        public Product() { }
    }

    //child 1
    public class Item : Product
    {
        public int id;
        public string name;
        public Item(int id)
        {
            this.id = id;
            this.name = "Item";
        }
    }

    //child 2
    public class Discount : Product
    {
        public int id;
        public string name;
        public Discount(int id)
        {
            this.id = id;
            this.name = "Discount";
        }
    }

List<ItemOrder> lst = new List<ItemOrder>();

var i = new Item(1);
var io = new ItemOrder(i);
lst.Add(io);

var d = new Discount(1);
var io2 = new ItemOrder(d);
lst.Add(io2);