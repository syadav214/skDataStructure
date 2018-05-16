//Merge 2 Linked List

function Node(data, next) {
    this.data = data;
    this.next = next;
}

function LinkedList() {
    this.currNode = null;
    this.smallerNode = null;
}

LinkedList.prototype = {
    add: function(data) {
        var newNode = new Node(data, this.currNode);
        this.currNode = newNode;
        return this.currNode;
    },
    print: function(head) {
        while (head) {
            console.log(head.data);
            head = head.next;
        }
    },
    mergeList: function(head1, head2) {
        if (head1 == null && head2 == null) {
            return null;
        } else if (head1 == null) {
            return head2;
        } else if (head2 == null) {
            return head1;
        }


        if (head1.data > head2.data) {
            head2.next = this.mergeList(head1, head2.next);
            return head2;
        } else {
            head1.next = this.mergeList(head1.next, head2);
            return head1;
        }
    }
}

var li = new LinkedList();
li.add(2);
var head1 = li.add(4);
//li.print(head1);

var li2 = new LinkedList();
li2.add(3);
var head2 = li2.add(1);
//li2.print(head2);

var li3 = new LinkedList();
var merge = li3.mergeList(head1, head2);
li3.print(merge);