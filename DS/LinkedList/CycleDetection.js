//To check if a node is visited

function Node(data, next) {
    this.data = data;
    this.next = next;
}

function LinkedList() {
    this.currnode = null;
}

LinkedList.prototype = {
    add: function(data) {
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
    hasCycle: function(head) {
        if (head == null) {
            return false;
        }

        var node = head;
        var visitedNode = [];
        var flag = 0;

        while (node) {
            if (visitedNode.includes(node)) {
                flag = 1;
                return true;
            } else {
                visitedNode.push(node);
            }
            node = node.next;
        }

        if (flag == 0) {
            return false;
        }
    }
}

var li = new LinkedList();
li.add(2);
li.add(3);
var head = li.add(4);
li.print(head);
console.log(li.hasCycle(head));