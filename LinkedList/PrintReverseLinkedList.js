//Print Linked List in reserve order.

function Node(data, next) {
    this.data = data;
    this.next = next;
}

function LinkedList() {
    this.currNode = null;
}

LinkedList.prototype = {
    add: function(data) {
        var newNode = new Node(data, this.currNode);
        this.currNode = newNode;
        return this.currNode;
    },
    printreverse: function(head) {
        if (head != null) {
            this.printreverse(head.next);
            console.log(head.data);
        }
    }
}

function main() {
    var li = new LinkedList();
    li.add(2);
    li.add(4);
    var head = li.add(5);
    li.printreverse(head);
    li.print();
}

main();