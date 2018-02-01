function Node(data, nextnode) {
    this.data = data;
    this.nextnode = nextnode;
}

function LinkedList() {
    this.currnode = null;
}

LinkedList.prototype = {
    addNode: function(data) {
        var newNode = new Node(data, this.currnode);
        this.currnode = newNode;
    },
    printList: function() {
        node = this.currnode;
        while (node) {
            console.log(node.data);
            node = node.nextnode;
        }
    }
}


var li = new LinkedList();
li.addNode(3);
li.addNode(5);
li.printList();