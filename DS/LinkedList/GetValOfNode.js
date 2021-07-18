// Find the node at the given position counting backwards from the tail

function Node(data, next) {
    this.data = data;
    this.next = next;
}

function LinkedList() {
    this.currnode = null;
}

LinkedList.prototype = {
    add: function add(data) {
        var newNode = new Node(data, this.currnode);
        this.currnode = newNode;
        return this.currnode;
    },
    print: function(head) {
        while (head) {
            console.log(head.data);
            head = head.next;
        }
    },
    getVal: function(head, pos) {
        var tempNode = head;
        var currpos = 0;
        while (head) {
            if (currpos > pos) {
                tempNode = tempNode.next;
            }
            head = head.next;
            currpos++;
        }
        console.log(tempNode.data);
    }
}

var li = new LinkedList();
li.add(2);
li.add(1);
var node1 = li.add(3);
li.print(node1);
li.getVal(node1, 0);