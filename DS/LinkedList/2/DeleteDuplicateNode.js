//Delete duplicate-value nodes from a sorted linked list

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
    deleteDuplicate: function(head) {
        if (head) {
            var test = head;
            while (head.next) {
                if (head.data == head.next.data) {
                    head.next = head.next.next;
                } else {
                    head = head.next;
                }
            }
            return test;
        }

    }
}

var li = new LinkedList();
li.add(2);
li.add(3);
var head1 = li.add(3);
li.print(head1);
console.log('________________')
var head2 = li.deleteDuplicate(head1);
li.print(head2);