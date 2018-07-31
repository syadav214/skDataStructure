//Reverse the LinkedList

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
    },
    printall: function() {
        var head = this.currnode;
        while (head != null) {
            console.log(head.data);
            head = head.next;
        }
    },
    reverseList: function() {
        var prev_head = null;
        var currentHead = this.currnode;
        while (currentHead != null) {
            var copy_prev_head = prev_head;
            var copy_currentHead_next = currentHead.next;

            prev_head = currentHead;
            currentHead.next = copy_prev_head;
            currentHead = copy_currentHead_next;
        }
        this.currnode = prev_head;
    }
}

var li = new LinkedList();
li.add(2);
li.add(4);
li.add(6);
li.reverseList();
li.printall();