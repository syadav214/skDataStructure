//Compare Linked List

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
    print: function(head) {
        while (head) {
            console.log(head.data);
            head = head.next;
        }
    },
    compare: function(headA, headB) {
        if (headA == null || headB == null) {
            return 0;
        } else {
            var unmatched = 0;
            while (headA && headB) {
                if (headA.data != headB.data) {
                    unmatched = 1;
                }
                headA = headA.next;
                headB = headB.next;
            }

            if (unmatched == 1) {
                return 0;
            } else {
                if (headA == null && headB != null) {
                    return 0;
                } else if (headB == null && headA != null) {
                    return 0;
                } else {
                    return 1;
                }
            }
        }
    }
}

var li = new LinkedList();
li.add(2);
li.add(6);
var headA = li.add(3);
//li.print(headA);
var li2 = new LinkedList();
li2.add(2);
li2.add(6);
var headB = li2.add(3);
console.log(li2.compare(headA, headB));